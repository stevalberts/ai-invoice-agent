ai_agent_project/
│── api/                            # API logic
│   │── __init__.py
│   │── main.py                     # FastAPI entry point
│   │── models.py                   # Pydantic models for validation
│   │── services.py                  # AI agent core logic
│   │── config.py                    # Configuration settings
│   │── routes/
│   │   │── __init__.py
│   │   │── agent.py                 # API routes for AI agent
│   │   │── health.py                # Health check routes
│
│── frontend/                        # Streamlit UI
│   │── __init__.py
│   │── app.py                       # Streamlit main interface
│   │── utils.py                     # Helper functions
│   │── components.py                 # UI components
│
│── tests/                           # Test cases
│   │── __init__.py
│   │── test_api.py                   # API tests
│   │── test_agent.py                 # AI agent tests
│
│── scripts/                         # Utility scripts
│   │── setup_env.py                  # Environment setup script
│
│── dataset/                            # Data files (if needed) https://github.com/zzzDavid/ICDAR-2019-SROIE/tree/master/data/img and https://data.mendeley.com/datasets/tnj49gpmtz/2
│
│── .env                             # Environment variables
│── uv.toml                          # uv dependency manager config
│── Dockerfile                       # Dockerfile for containerization
│── README.md                        # Project documentation
│── .gitignore                       # Git ignore file
│── run.py                           # Script to run API & Streamlit
