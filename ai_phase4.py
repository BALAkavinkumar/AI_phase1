def load_Dataset(data,size=None):
    
    if(size!=None):
        y,X=data[:size]
    else:
        y,X=data
        
    X_tokenizer=tokenize(X)
    y_tokenizer=tokenize(y)
    
    X_tensor=vectorization(X_tokenizer,X)
    y_tensor=vectorization(y_tokenizer,y)
    
    return  X_tensor,X_tokenizer, y_tensor, y_tokenizer
