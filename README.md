# project\_V5\_15

Project for Module V5\_15 "Developing Software as s Product" at ZHAW, ACLS, by Anika Heim, Philipp Osterwalder and Michelle Schmid for the course project in SS26. The game is called "Game of Life" and simulates the growth and development of a city over time.



## Description



This game is called “Game of Life.” Various structures from the real world are replicated on a playing field, such as land, water, houses, roads, people, and cars. The game can be started either with a real map or a random map. Every second, the playing field is updated and displayed in the terminal. With each update of the map, it is changed by moving vehicles, a growing population, a dynamic economy, etc. The game is currently still quite simple and has some features that could be improved. For example, the game currently only has one type of house, but it could be expanded to include different types of houses with varying capacities and costs. Additionally, the game could be made more interactive by allowing the player to make decisions that affect the growth and development of the city, such as building new roads or investing in certain industries. Overall, the game is a fun and engaging way to simulate the growth and development of a city over time.

### Project structre



```
project_V5_15/
│── pics/               # Picutres used in the game for the map
│── skripts/            # Source code
│   ├── Play.py/        # contains the main game loop and user interaction
│   └── utils/          # Helper functions
│── tests/              # Unit tests
│── .vscode/            # VSCode configuration files (pytest and python debugger settings)
│── requirements.txt    # Dependencies
│── main.py             # Entry point (if applicable)
│── README.md
│── .gitignore          # Git ignore file
│── .gitattributes      # Git attributes file
│── LICENSE.md          # License information
│── pytest.ini          # Pytest configuration
```


## Getting Started

### Dependencies

To run the game, you will need to have Python 3.8 or higher installed on your system. Additionally, the game relies on several external libraries, which are listed in the requirements.txt file. You can install these dependencies using pip, the Python package installer, by running the following command in your terminal:

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



### Executing program
4. Run the project
```
python Play.py
```


## Help



If you have any questions or need further assistance, please feel free to contact the authors or open an issue in the GitHub repository.



## Authors

- Michelle Schmid ([github.com/schmimmim]()
- Philipp Osterwalder ([github.com/R0b0000007]()
- Anika Heim ([github.com/anika-dot]()



## Version History

&#x20;   \* Initial Release - 0.1 - 2026-05-11


## License



This project is licensed under the \[MIT] License - see the LICENSE.md file for details.