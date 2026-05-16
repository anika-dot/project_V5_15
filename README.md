# project\_V5\_15

A city simulation game developed as part of the Module V5_15 "Developing Software as a Product" at ZHAW, ACLS. Created by Anika Heim, Philipp Osterwalder, and Michelle Schmid for the course project in Spring Semester 2026 (SS26).



## Description

This game is called “Game of Life.” Various structures from the real world are replicated on a playing field, such as land, water, houses, roads, people, and cars. The game can be started either with a real map or a random map. Every second, the playing field is updated and displayed in the terminal. With each update of the map, it is changed by moving vehicles, a growing population, a dynamic economy, etc. The game is currently still quite simple and has some features that could be improved. For example, the game currently only has one type of house, but it could be expanded to include different types of houses with varying capacities and costs. Additionally, the game could be made more interactive by allowing the player to make decisions that affect the growth and development of the city, such as building new roads or investing in certain industries. Overall, the game is a fun and engaging way to simulate the growth and development of a city over time.

### Project structre

```
project_V5_15/
│── pics/               # Images used for map visualization
│── skripts/            # Source code
│   ├── Play.py         # Main game loop and user interaction
│   └── utils/          # Helper functions and modules
│── tests/              # Unit tests
│── .vscode/            # VSCode settings (pytest, debugger)
│── requirements.txt    # Python dependencies
│── main.py             # Entry point (if applicable)
│── README.md           # Project documentation
│── .gitignore          # Git ignore rules
│── .github/            # CI/CD workflow configuration
│── .gitattributes      # Git attributes
│── LICENSE.md          # License information
│── pytest.ini          # Pytest configuration
```


## Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package installer)
- Install dependencies listed in requirements.txt:

```
pip install -r requirements.txt
```

### Installing
1. Clone the repository:
```
git clone https://github.com/anika-dot/project_V5_15.git
cd project_V5_15
```

3. Create a virtual environment
```
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```
4. Install dependencies
```
pip install -r requirements.txt
```

### Running the game
4. Run the project
```
python skripts/Play.py
```

## Features
- Procedural or map-based world generation
- Real-time simulation updated every second
- Dynamic population, economy, and vehicle behaviors
- Modular architecture for easy feature expansion

Planned improvements:
- Multiple house types with unique attributes
- Interactive gameplay (e.g., build roads, manage industries)
- Enhanced visuals and user interface

## Testing
Run all tests using pytest:
```
pytest
```


## Help
If you encounter issues:

- Check your Python version (python --version)
- Ensure all dependencies are installed
- Open an issue on https://github.com/anika-dot/project_V5_15/issues


## Authors

- Michelle Schmid ([github.com/schmimmim]())
- Philipp Osterwalder ([github.com/R0b0000007]())
- Anika Heim ([github.com/anika-dot]())



## Version History

&#x20;   \* Initial Release - 0.1 - 2026-05-11


## License


This project is licensed under the \[MIT] License - see the LICENSE.md file for details.