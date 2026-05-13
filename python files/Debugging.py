import logging

logging.basicConfig(
    filename='script_history.log', 
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("User logged in successfully.")
logging.debug("Database connection established.")