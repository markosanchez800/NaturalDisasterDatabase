# Natural Disaster DB

## Impacts and Vision
Natural disasters such as hurricanes, floods, wildfires, earthquakes, and severe storms affect communities throughout the United States every year. Information about these disasters can be difficult to understand when it is spread across many records. The motivation for this project is to create an application that organizes natural-disaster information in a searchable database. The goal of the Natural Disaster Database and Tracker is to allow users to search historical disasters based on location, disaster type, and date. Users could answer questions such as which states have experienced the most federally declared disasters, what types of disasters occur most frequently, and how the number of disasters has changed over time. The application would make historical disaster information easier to explore while demonstrating how Python and databases can be used to analyze real-world public data.

## Getting Started

### Install Dependencies

Below are a list of 3rd party libraries used in this project. Be sure to install them into your environment before developing this project.

```sh
pip install pandas kaggle matplotlib scikit-learn sqlite3
```

### Obtaining the Dataset

Run this command at the root of this repository folder:

```sh
mkdir -p data
kaggle datasets download -d brsdincer/all-natural-disasters-19002021-eosdis -p data --unzip
```