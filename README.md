# Lab 3
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
Carrie Lei
Ishraq Rahman

## Lab Question Answers

Question 1: 
Restful APIs are scalable because the client and server are separated. Specifically, the server side is stateless, so it doesn't need to store anything across requests. This minimal need for client-server communication is what makes it more scalable and allows for more types of data formats (besides XML) to be used.

Question 2:
According to the definition of "resources" provided in the AwS article, the resources the mail server is providing to clients is authentication and proxy services for the interal and external client connections. (https://learn.microsoft.com/en-us/exchange/architecture/client-access/client-access?view=exchserver-2019) (Ishraq Rahman)

Answer for Question 3: 
The PUT methond is the REST Method not used in out mail server. We can extend out server to use this method by creating a function that will require a set of three parameters, the url, params or data, and the arguments. (Ishraq Rahman)

Answer for Question 4:
API keys are used for many RESTful APIs as a way to authorize and authenticate API requests from the client. This way, the server can track and identify individual clients, monitor usage, and enforce rate limiting and other access controls (preventing unauthorized access and abuse of the API). (https://cloud.google.com/endpoints/docs/openapi/when-why-api-key) 
