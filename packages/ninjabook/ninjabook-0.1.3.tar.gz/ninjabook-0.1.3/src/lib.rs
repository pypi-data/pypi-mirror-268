use pyo3::prelude::*;
use std::cmp::Ordering;
use std::collections::BTreeMap;

#[derive(Debug, Default, Clone)]
#[pyclass]
pub struct Orderbook {
    best_bid: Option<Level>,
    best_ask: Option<Level>,
    bids: BTreeMap<u64, Level>,
    asks: BTreeMap<u64, Level>,

    #[pyo3(get)]
    last_updated: u64,

    #[pyo3(get)]
    last_sequence: u64,

    inv_tick_size: f64,
}

#[pymethods]
impl Orderbook {
    #[new]
    pub fn new(tick_size: f64) -> Self {
        Self {
            best_bid: None,
            best_ask: None,
            bids: BTreeMap::new(),
            asks: BTreeMap::new(),
            last_updated: 0,
            last_sequence: 0,
            inv_tick_size: 1.0 / tick_size,
        }
    }

    #[inline]
    pub fn process(&mut self, event: Event) {
        if event.timestamp < self.last_updated || event.seq < self.last_sequence {
            return;
        }

        match event.is_trade {
            true => self.process_trade(event),
            false => self.process_lvl2(event),
        };

        self.last_updated = event.timestamp;
        self.last_sequence = event.seq;
    }

    #[inline]
    pub fn process_stream_bbo(&mut self, event: Event) -> Option<(Option<Level>, Option<Level>)> {
        let old_bid = self.best_bid;
        let old_ask = self.best_ask;

        self.process(event);

        let new_bid = self.best_bid;
        let new_ask = self.best_ask;

        if old_bid != new_bid || old_ask != new_ask {
            Some((new_bid, new_ask))
        } else {
            None
        }
    }

    #[inline]
    fn process_lvl2(&mut self, event: Event) {
        let price_ticks = event.price_ticks(self.inv_tick_size);
        match event.is_buy {
            true => {
                if event.size == 0.0 {
                    if let Some(removed) = self.bids.remove(&price_ticks) {
                        if let Some(best_bid) = self.best_bid {
                            if removed.price == best_bid.price {
                                self.best_bid = self.bids.values().next_back().cloned();
                            }
                        };
                    }
                } else {
                    self.bids
                        .entry(price_ticks)
                        .and_modify(|e| e.size = event.size)
                        .or_insert(Level::from(event));

                    let Some(best_bid) = self.best_bid else {
                        self.best_bid = Some(Level::from(event));
                        return;
                    };

                    if event.price >= best_bid.price {
                        self.best_bid = Some(Level::from(event));
                    }
                }
            }
            false => {
                if event.size == 0.0 {
                    if let Some(removed) = self.asks.remove(&price_ticks) {
                        if let Some(best_ask) = self.best_ask {
                            if removed.price == best_ask.price {
                                self.best_ask = self.asks.values().next().cloned();
                            }
                        };
                    }
                } else {
                    self.asks
                        .entry(price_ticks)
                        .and_modify(|e| e.size = event.size)
                        .or_insert(Level::from(event));

                    let Some(best_ask) = self.best_ask else {
                        self.best_ask = Some(Level::from(event));
                        return;
                    };

                    if event.price <= best_ask.price {
                        self.best_ask = Some(Level::from(event));
                    }
                }
            }
        }
    }

    #[inline]
    fn process_trade(&mut self, event: Event) {
        let buf = match event.is_buy {
            true => &mut self.bids,
            false => &mut self.asks,
        };

        let price_ticks = event.price_ticks(self.inv_tick_size);

        if let Some(level) = buf.get_mut(&price_ticks) {
            if event.size >= level.size {
                buf.remove(&price_ticks);
            } else {
                level.size -= event.size;
            }
        };
    }

    pub fn best_bid(&self) -> Option<Level> {
        self.best_bid
    }

    pub fn best_ask(&self) -> Option<Level> {
        self.best_ask
    }

    #[inline]
    pub fn top_bids(&self, n: usize) -> Vec<Level> {
        self.bids.values().rev().take(n).cloned().collect()
    }

    #[inline]
    pub fn top_asks(&self, n: usize) -> Vec<Level> {
        self.asks.values().take(n).cloned().collect()
    }

    #[inline]
    pub fn midprice(&self) -> Option<f64> {
        if let (Some(best_bid), Some(best_ask)) = (self.best_bid, self.best_ask) {
            return Some((best_bid.price + best_ask.price) / 2.0);
        }

        None
    }

    #[inline]
    pub fn weighted_midprice(&self) -> Option<f64> {
        if let (Some(best_bid), Some(best_ask)) = (self.best_bid, self.best_ask) {
            let num = best_bid.size * best_ask.price + best_bid.price * best_ask.size;
            let den = best_bid.size + best_ask.size;
            return Some(num / den);
        }

        None
    }
}

#[derive(Debug, Clone, Copy, Default)]
#[pyclass]
pub struct Level {
    #[pyo3(get)]
    pub price: f64,

    #[pyo3(get)]
    pub size: f64,
}

#[pymethods]
impl Level {
    #[new]
    pub fn new() -> Self {
        Self {
            price: 0.0,
            size: 0.0,
        }
    }

    fn __str__(&self) -> String {
        format!("Level(price: {}, size: {})", self.price, self.size)
    }
}

#[allow(clippy::non_canonical_partial_ord_impl)]
impl PartialOrd for Level {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        match self.price.partial_cmp(&other.price) {
            Some(Ordering::Equal) => self.size.partial_cmp(&other.size),
            other_order => other_order,
        }
    }
}

impl Ord for Level {
    fn cmp(&self, other: &Self) -> Ordering {
        self.partial_cmp(other).unwrap()
    }
}

impl PartialEq for Level {
    fn eq(&self, other: &Self) -> bool {
        self.price == other.price && self.size == other.size
    }
}

impl Eq for Level {}

impl From<Event> for Level {
    fn from(value: Event) -> Self {
        Self {
            price: value.price,
            size: value.size,
        }
    }
}

#[derive(Debug, Clone, Copy)]
#[pyclass]
pub struct Event {
    #[pyo3(get)]
    pub timestamp: u64,

    #[pyo3(get)]
    pub seq: u64,

    #[pyo3(get)]
    pub is_trade: bool,

    #[pyo3(get)]
    pub is_buy: bool,

    #[pyo3(get)]
    pub price: f64,

    #[pyo3(get)]
    pub size: f64,
}

#[pymethods]
impl Event {
    #[new]
    pub fn new(
        timestamp: u64,
        seq: u64,
        is_trade: bool,
        is_buy: bool,
        price: f64,
        size: f64,
    ) -> Self {
        Self {
            timestamp,
            seq,
            is_trade,
            is_buy,
            price,
            size,
        }
    }

    fn __str__(&self) -> String {
        format!(
            "Event(timestamp: {}, size: {}, is_trade: {}, is_buy: {}, price: {}, size: {})",
            self.timestamp, self.seq, self.is_trade, self.is_buy, self.price, self.size
        )
    }

    pub fn price_ticks(&self, tick_size: f64) -> u64 {
        (self.price * tick_size) as u64
    }
}

#[pymodule]
fn ninjabook(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<Event>()?;
    m.add_class::<Level>()?;
    m.add_class::<Orderbook>()?;
    Ok(())
}
