# 🌦️ WeatherAlertApp

A modular Python Command Line Interface (CLI) application that queries live weather data for any given city, logs the structured JSON data locally, and instantly dispatches a push notification via Telegram if inclement rainy weather is detected in the upcoming forecast.

---

## 🚀 Key Features

* **Interactive CLI Interface:** Seamless terminal prompt allowing users to quickly look up target global cities.
* **Automated Data Pipeline:** Pulls multi-day weather metadata, automatically formats the contents, and commits it locally to an isolated directory.
* **Smart Rain Detection:** Scans upcoming structural forecast parameters to determine precipitation probability.
* **Instant Telegram Telegram Alerts:** Communicates securely with the Telegram Bot API to drop instant mobile notifications to specific chat endpoints.
* **Production Containerization:** Ships with a ready-made deployment pipeline utilizing Docker.
* **Isolated Environment Configurations:** Keeps sensitive credentials separated via an environment variable configuration template.

---

## 📁 Repository Blueprint

```text
WeatherAlertApp/
├── Saved Json Files/        # Local persistent forecast storage
│   └── weather_data.json    # Cached payload response from the weather client
├── scripts/                 # Core sub-system modules
│   ├── alert_sender.py      # Communication script interfacing with the Telegram Bot API
│   ├── data_saver.py        # Logic module managing file system creation and writing
│   └── weather_puller.py    # Request handler communicating with the external weather engine
├── .gitignore               # System file keeping development secrets offline
├── Dockerfile               # Blueprint instructions for cross-platform image isolation
├── README.md                # General technical project manual
├── main.py                  # Operational CLI entry point file for system execution
├── requirements.txt         # Registry tracking external dependency libraries
└── tokens.env               # Sensitive credentials file (Excluded from version control)
```

---

## 🛠️ Local Installation & Environment Configurations

### 1. Repository Setup
Clone this repository to your local workspace environment:
```bash
git clone https://github.com
cd WeatherAlertApp
```

### 2. Dependency Management
Install the necessary system pipeline modules compiled in your tracking registry:
```bash
pip install -r requirements.txt
```

### 3. Environment Variables Configuration
To run successfully, the program reads variables natively out of a custom configurations template. Create a file in the project's root folder named **`tokens.env`** and feed it your specific values:

```env
TELEGRAM_BOT_TOKEN=your_bot_token_generated_by_botfather
USER_INFO_ID=your_personal_telegram_chat_id
```
*(Note: To safeguard credentials, `tokens.env` is caught by your `.gitignore` configuration rule and will never build into upstream version control tracking).*

---

## 💻 Code Execution

Natively fire up the core user-interface application pipeline:
```bash
python main.py
```

---

## 🐳 Application Containerization (Docker Workflow)

This system provides a full container recipe allowing you to deploy the script inside a platform-agnostic sandbox context.

### 1. Compile the Sandbox Environment Image
```bash
docker build -t weather-alert-app .
```

### 2. Launch the Application Image Context
Pass your native authentication parameters directly into the running instance during initiation:
```bash
docker run -it --env-file tokens.env weather-alert-app
```

---

## 🛠️ Architecture Deep-Dive

* **`main.py`**: The terminal orchestration loop. Takes input arguments, handles flow management, and acts as the project controller.
* **`scripts/weather_puller.py`**: Interacts with the backend Open-Meteo weather APIs to handle coordinate transformations and pull real-time structural forecast arrays.
* **`scripts/data_saver.py`**: Verifies pathing safety and records network data models cleanly to disk inside the local persistence directory.
* **`scripts/alert_sender.py`**: Compiles payloads and structures low-level POST requests directly into Telegram's API gateways to ensure phone notification delivery.
