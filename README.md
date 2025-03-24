<h1 align="center">
  Topic Modeling Playground
</h1>
<div align="center">
  
  <a href="">![Static Badge](https://img.shields.io/badge/Word2Vec-blue)</a>
  <a href="">![Static Badge](https://img.shields.io/badge/Glove-green)</a>
  <a href="">![Static Badge](https://img.shields.io/badge/LDA-red)</a>
  <a href="">![Static Badge](https://img.shields.io/badge/BERTopic-yellow)</a>
  
</div>

<p align="center">
  A review of the most popular topic modeling techniques.
</p>

<div align="center">
  <a href="https://www.researchgate.net/profile/Mauro-Bruno-2">
    <img src="https://img.shields.io/badge/Mauro%20Bruno-white?logo=researchgate" alt="Mauro Bruno">
  </a>
  <a href="https://www.researchgate.net/profile/Elena-Catanese-2">
    <img src="https://img.shields.io/badge/Elena%20Catanese-white?logo=researchgate" alt="Elena Catanese">
  </a>
  <a href="https://www.researchgate.net/profile/Francesco-Ortame-3">
    <img src="https://img.shields.io/badge/Francesco%20Ortame-white?logo=researchgate" alt="Francesco Ortame">
  </a>
</div>

---
This repository contains the code for hands-on sessions related to topic modeling. It is designed to help you understand the concepts and implementations of topic modeling techniques, including but not limited to LDA (Latent Dirichlet Allocation) and more advanced approaches based on word embeddings, such as BERTopic.

## Prerequisites

Before you begin, ensure you have the following software installed:

- Python 3.7 or higher
- Required Python libraries (listed below)

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/mauroIstat/word-embedding-tutorial.git
cd word-embedding-tutorial
```

### Install Dependencies

You can install the required dependencies using pip. It is recommended to create a virtual environment before installing the packages.

```bash
pip install -r requirements.txt
```

The `requirements.txt` file includes the following libraries:

- pandas
- numpy
- scikit-learn
- gensim
- matplotlib
- pyLDAvis
- bertopic

### Additional Resources

- [Gensim Documentation](https://radimrehurek.com/gensim/)
- [BERTopic Documentation](https://github.com/MaartenGr/BERTopic)

## Usage

To run the notebooks or scripts for topic modeling:

1. Download and preprocess the dataset (if not already available).
2. Explore the code and try running different techniques for topic modeling.
3. Use the provided Jupyter Notebooks or Python scripts for each part of the tutorial.


## File Structure

- `data/`: Sample datasets used for the tutorial.
- `papers/`: Papers on Wordembedding techniques (Word2Vec & Glove).
- `resources/`: An extended list of Italian stopword and the Italian .pickle file needed to tokenize text.
- `src/`: Utility functions in python.

## Contributing

If you'd like to contribute to the repository, feel free to fork it and submit a pull request. Please make sure your code adheres to the existing coding standards and includes tests where necessary.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
