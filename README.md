# toy_deployment
Deploy Toy ML model with FastAPI and docker.

## How to use
1 - Clone repo   
2 - Run 
```
sudo sh start_service.sh
```  
3 - Copy paste in browser
```  
http://localhost:8000/docs
```  
Or to test with POSTMAN for GET sanity check: 
```
http://localhost:8000/
```

and for POST request:
```  
http://localhost:8000/QA/
```  

Exemple: 
{
 "context": "Manuel Romero has been working hardly in the repository hugginface/transformers lately",
 "question": "Who has been working hard for hugginface/transformers lately?"
 }
