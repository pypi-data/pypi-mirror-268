#![allow(non_local_definitions)]
use pyo3::prelude::*;
use pyo3::types::{PyString, PyType};
use seq_macro::seq;
use vizitig_lib::dna::{Nucleotid, DNA};
use vizitig_lib::iterators::CanonicalKmerIterator;
use vizitig_lib::kmer::ShortKmer;

#[pyclass(name = "DNA")]
pub struct PyDNA {
    pub content: DNA,
}

seq!(N in 3..=31{
#[pymethods]
impl PyDNA {

    #[new]
    pub fn new<'py>(input_pystr: &'py PyString) -> PyResult<Self> {
        let input_str = input_pystr.to_str()?;
        let dna = input_str.as_bytes().try_into().unwrap();
        Ok(PyDNA {
            content: dna
        })
   }

    pub fn __repr__(&self) -> PyResult<String> {
        Ok(self.content.content.clone().into_iter().map(|u| char::from(u)).collect::<String>())
    }

    fn __len__(&self) -> PyResult<usize>{
        Ok(self.content.content.len())
    }

    pub fn get_index(&self, index: usize) -> PyResult<char>{
        Ok(self.content.content[index].into())
    }
    pub fn get_slice(&self, start: usize, stop: usize) -> PyResult<Self> {
        Ok(PyDNA {
            content: DNA {
                content: self.content.content.get(start..stop).unwrap().to_vec()
            }
        })
    }

    #(
    pub fn enumerate_canonical_kmer~N(&self) -> PyResult<Vec<PyKmer~N>>{
        let it : CanonicalKmerIterator<N, u64> = (&self.content).try_into().unwrap();
        Ok(it.map(|u| PyKmer~N{content: u }).collect())
    }
    )*

}
});

seq!(N in 3..=31{
#[pyclass(name="Kmer")]
#[derive(Clone)]
pub struct PyKmer~N{
    content: ShortKmer<N>,
}
#[pymethods]
impl PyKmer~N{
    #[classmethod]
    fn from_dna(_: &PyType, dna: &PyDNA) -> PyResult<Self>{
        let nucleotids : &[Nucleotid; N] = dna.content.content.first_chunk::<N>().unwrap();
        let kmer : ShortKmer<N> = nucleotids.try_into().unwrap();
        Ok(PyKmer~N{ content: kmer })
    }

    fn add_left_nucleotid(&self, n: char) -> PyResult<Self>{
        Ok(PyKmer~N{ content: self.content.append_left(n.try_into().unwrap()) })
    }


    fn add_right_nucleotid(&self, n: char) -> PyResult<Self>{
        Ok(PyKmer~N{ content: self.content.append(n.try_into().unwrap()) })
    }

    fn __repr__(&self) -> PyResult<String>{
        return Ok(format!("{}", &self.content))
    }

    fn __str__(&self) -> PyResult<String>{
        return Ok((&self.content).into())
    }

    fn __lt__(&self, other: Self) -> PyResult<bool> {
        return Ok(self.content <= other.content)
    }

    fn __gt__(&self, other: Self) -> PyResult<bool> {
        return Ok(self.content >= other.content)
    }
}
});


seq!(N in 3..=31{
#[pymodule]
fn _vizibridge(_py: Python, m: &PyModule) -> PyResult<()> {
    #(
        m.add_class::<PyKmer~N>()?;
    )*
    m.add_class::<PyDNA>()?;
    Ok(())
}});
