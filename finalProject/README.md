# Personal Finance CLI

A small command-line application to track personal finances (income and expenses), persist them to a JSON file, and view summaries and filtered reports.

**Requirements:**

- **Python:** >= 3.12
- **Dependencies:** pydantic, pyfiglet, tabulate (for runtime) and pytest (for tests). Install with `pip install pydantic pyfiglet tabulate pytest` or via your preferred environment manager.

**Installation:**

- Clone the repository and change into the `finalProject` folder.
- Install dependencies: `pip install pydantic pyfiglet tabulate pytest`

**Usage:**

- Run the CLI from the `finalProject` directory:

```bash
python main.py
```

- Follow the interactive prompts to add transactions, show lists, filter by type or period, delete a transaction, or delete all data.

**Commands / Options (interactive menu):**

- **Add a transaction:** enter title, description, date (multiple formats accepted), tags, amount, and type (Income/Expense).
- **Show all transactions:** displays a table and totals (income, expense, balance).
- **Show transactions by type:** filter either `income` or `expense` and see the total for that type.
- **Show transactions by period:** choose `custom`, `month-year`, or `year` and provide the date(s) to filter.
- **Delete transaction:** remove a single transaction by its index.
- **Delete all data:** permanently remove `finance.json` (must confirm by typing `DELETE`).

**Data storage:**

- Transactions are stored in `finance.json` in the project folder by default. The file is created automatically on the first save.

**Project files:**

- **Code:** [finalProject/main.py](finalProject/main.py), [finalProject/services.py](finalProject/services.py), [finalProject/model.py](finalProject/model.py)
- **Constants:** [finalProject/constants.py](finalProject/constants.py)
- **Data file:** [finalProject/finance.json](finalProject/finance.json)
- **Tests:** [finalProject/test_main.py](finalProject/test_main.py), [finalProject/test_services.py](finalProject/test_services.py), [finalProject/test_model.py](finalProject/test_model.py)

**Testing:**

- From the `finalProject` directory run: `pytest` — the test suite verifies input handling, service behavior, JSON persistence, and report logic.

**Notes & Tips:**

- The CLI accepts several date formats (YYYY-MM-DD, MM/DD/YYYY, DD/MM/YYYY, YYYY/MM/DD).
- Titles must be > 5 characters and descriptions <= 255 characters — input is validated by `pydantic` models.
- Use `Ctrl+C` or `Ctrl+D` to exit the interactive prompt safely.
