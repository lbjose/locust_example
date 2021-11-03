import time
from locust import HttpUser, task, between, tag


class RunStats(HttpUser):
    """
        Here we define a class that will be used to get the time estimates for a given API.

        To check more about the locust visit http://docs.locust.io/en/stable/what-is-locust.html

        The class inherits the HttpUser which gives the client attribute to each user, this attribute can be used to
        make HTTP requests to the target system that we want to load test.

        To run the script you can use:
            - locust, filename needs to be locustfile.py
            - locust -f file_name -H HOST

        Open http://localhost:8089/, to see the results in the browser.

        To have the results saved as csv you can checkout http://docs.locust.io/en/stable/retrieving-stats.html

        - You can have multiple tasks assigned and add weight to those tasks.
        - You can also add on_start and on_stop functions to execute any work on start and on stop of task
        - You can give tag name to each task and call those tasks only from command line using --tags argument.
    """

    @tag("sbert")
    @task
    def get_stats_sbert(self):
        """
            The function calls the API with two sentences to compare using SBERT.

            To learn more about SBERT, visit https://www.sbert.net/
        """
        sent1 = "A man is eating food."
        sent2 = "A man is eating pasta."
        self.client.post("http://0.0.0.0:8001/get_similarity_score", data={"sent1": sent1, "sent2": sent2})

    @tag("USE")
    @task
    def get_stats_bert(self):
        """
            The function calls the API with two sentences to compare using Universal Sentence Encoder (USE).

            To learn more about USE, visit https://tfhub.dev/google/universal-sentence-encoder/1
        """
        sent1 = "A man is eating food."
        sent2 = "A man is eating pasta."
        self.client.post("http://0.0.0.0:8001/get_similarity_score", data={"sent1": sent1, "sent2": sent2})