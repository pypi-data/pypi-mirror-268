from IPython.core.magic import (Magics, magics_class, line_magic,
                                cell_magic, line_cell_magic,get_ipython)
import requests
import dill
import base64
import VizKG.visualize as vkg

@magics_class
class LabMagic(Magics):

    def __init__(self):
        super(LabMagic,self).__init__(None)
        self.knowledge_graph = None
        self.PUBLIC_IPV4_ADDRESS_AWS_EC2_INSTANCE = None
        self.chart = None

    @line_magic
    def set_ipv4(self,line):
        """
        Set the ipv4 address.

        Args:
            line (str): the ipv4 address
        """
        if len(line) != 0:
            self.PUBLIC_IPV4_ADDRESS_AWS_EC2_INSTANCE = line
            print("The address is correctly loaded ! ")
            print(f"The public ipv4 address is {self.PUBLIC_IPV4_ADDRESS_AWS_EC2_INSTANCE}")
        else :
            print("Please enter an address")
    
    @line_magic
    def set_kg(self,line):
        """
        Set the knowledge graph.

        Args:
            line (str): name of the knowledge graph
        """
        if len(line)!=0:
            self.knowledge_graph = line
            print("The knowledge graph is correctly loaded !")
            print(f"The knowledge graph is {self.knowledge_graph}")
        else:
            print("Please etner a knowledge graph")

    @line_magic
    def ask(self,line):
        """
        Print the result of the question, and show the first visualization.

        Args:
            line (str): the question to ask
        """
        response = self.send_request_to_ec2(line,self.knowledge_graph)
        if response != None and response != []:
            try:
                response[0]['chart'].plot()
            except Exception as e:
                pass

            prettier_results = self.prettier_results(results=response)
            for result in prettier_results:
                print(result)

    def send_request_to_ec2(self,question, knowledge_graph, max_answers=3):
        """
        Send a POST request to an AWS EC2 instance.

        Parameters:
            url (str): The URL to send the request to, including the EC2 instance's address.
            question (str): The question to ask.
            knowledge_graph (str): The name of the knowledge graph to use.
            max_answers (int): The maximum number of answers to return.

        Returns:
            response.json() (dict): The JSON response from the server if the request is successful.
            None: If the request fails.
        """
        headers = {"Content-Type": "application/json"}
       
        data = {
            "question": question,
            "knowledge_graph": knowledge_graph,
            "max_answers": max_answers,
            "chart_type": None
            }
        url = "http://" + self.PUBLIC_IPV4_ADDRESS_AWS_EC2_INSTANCE + "/post"
        try:
            response = requests.post(url, json=data, headers=headers)
            response.raise_for_status()  # Raises an exception for 4XX/5XX errors
            return self.decode_chart(response.json())  # Returns the JSON response from the server
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def decode_chart(self,response):
        """
        Decode the encoded chart

        Parameters:
            response (dict): The JSON response from the server if the request is successful.

        Returns:
            decoded_response (dict): The JSON response with decode chart
        """
        coded_to_chart = lambda s: dill.loads(base64.b64decode(s))
        for answer in response:
            answer['chart'] = coded_to_chart(answer['chart'])

        return response
        
    def prettier_results(self,results):
        return [(result["values"][0], result["score"]) for result in results]
    
    @line_magic
    def show_parameters(self):
        """
        Show the ipv4 address and the knowledge graph
        """
        print(f"The public ipv4 address is {self.PUBLIC_IPV4_ADDRESS_AWS_EC2_INSTANCE}")
        print(f"The knowledge graph is {self.knowledge_graph}")


def load_ipython_extension():
    lab_magic = LabMagic()
    get_ipython().register_magics(lab_magic)