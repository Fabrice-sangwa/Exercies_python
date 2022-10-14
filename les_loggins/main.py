import logging

logging.basicConfig(level=logging.DEBUG,
                    filename=r"les_loggins/app.log",
                    encoding="utf-8",
                    filemode="w",
                    format= '%(asctime)s - %(levelname)s - %(message)s'
                    )

logging.debug("La fonction a bien été exécuté ")
logging.info("Meessage d'information pour l'utilisateur")
logging.warning("Message d'avertissement")
logging.error("une erreur est survenue")
logging.critical("Erreur fatale d'exécution")


