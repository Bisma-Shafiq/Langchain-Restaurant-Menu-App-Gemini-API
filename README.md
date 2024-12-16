# Restaurant Menu Item GenAI App


This project leverages **Google Generative AI (Gemini-1.5)** and the **LangChain** framework to create a dynamic application that generates:

1. Fancy names for restaurants based on a specific cuisine.
2. Unique menus with 5-6 signature dishes tailored to the restaurant's cuisine.

The project is designed to inspire creativity for entrepreneurs in the food industry and demonstrate the capabilities of cutting-edge AI tools.

---

## Features
- **Dynamic Name Generation**: Create fancy, creative, and memorable names for your restaurant.
- **Customized Menus**: Generate menus with signature dishes that perfectly match the selected cuisine.
- **Seamless Chaining**: Combines multiple AI tasks into a single streamlined workflow using **LangChain SequentialChain**.

---

## Tools & Technologies

### Core Tools:
- **[Google Generative AI (Gemini-1.5)](https://developers.generativeai.google/)**: Generates high-quality text outputs with contextual understanding.
- **LangChain**: A framework for building applications powered by language models.

### Python Libraries:
- `google.generativeai`: Python SDK for interacting with Google Generative AI.
- `langchain_google_genai`: LangChain integration with Google Generative AI.
- `langchain`: Orchestrates prompts and chains for AI workflows.
- `dotenv`: Loads environment variables securely from a `.env` file.

---

## Installation & Setup

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Set Up Virtual Environment (Optional)**:
   ```bash
   python -m venv env
   source env/bin/activate   # For Linux/Mac
   env\Scripts\activate     # For Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Add Your Google API Key**:
   - Create a `.env` file in the project root directory.
   - Add your Google Generative AI API key to the file:
     ```env
     GOOGLE_API_KEY=your_google_api_key_here
     ```

---

## Usage

### Run the Application

1. Import the `generate_items` function into your Python script or interactive session.
2. Call the function with the desired cuisine:
   ```python
   from generator import generate_items

   response = generate_items("Italian")
   print("Restaurant Name:", response["restaurant_name"])
   print("Menu Items:", response["menu_items"])
   ```
3. Example Output:
   ```plaintext
   Restaurant Name: Bella Cucina
   Menu Items:
   - Truffle Mushroom Risotto
   - Classic Margherita Pizza
   - Lobster Ravioli in Creamy Sauce
   - Tiramisu Delight
   - Handmade Gnocchi with Pesto
   ```

---

## Project Structure
```
.
├── generator.py          # Core script for generating restaurant names and menus
├── .env                  # Environment file (contains API key)
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── ... (other files as needed)
```

---

## How It Works

1. **Prompt Templates**: Two custom prompts are defined for generating the restaurant name and menu items.
2. **LLMChain**: Each prompt is connected to a separate chain for individual processing.
3. **SequentialChain**: Combines the individual chains into a cohesive workflow, passing the restaurant name to the menu generation step.
4. **Response**: Outputs the generated restaurant name and menu items as a dictionary.

---

## Requirements
- Python 3.8+
- A valid Google Generative AI API key

---

## Contributing
Feel free to contribute to this project by submitting issues or pull requests. Please follow the [contribution guidelines](CONTRIBUTING.md) if you want to get involved.


---

## Acknowledgments
Special thanks to:
- **Google Generative AI Team** for providing such powerful AI tools.
- The creators of **LangChain** for simplifying AI workflows.

---

## Author
**Bisma Shafiq**

Connect with me on [LinkedIn](https://www.linkedin.com/in/bisma-shafiq-3a3b31242/)!
