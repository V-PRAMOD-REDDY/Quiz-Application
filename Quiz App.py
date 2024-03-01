if __name__=="__main__":
    #-------------------------Quiz Questions-----------------------------
    que=["Who is the father of python?",
         "What is a correct syntax to output 'Hello World' in Python ?",
         "How do you insert COMMENTS in Python code?"]
    #-------------------------Quiz Options--------------------------------
    ans=["""A.Charles Babbage\nB.Guido van Rossum \nC.Dennis Ritchie \nD.None of the above""",
         """A.print("Hello World"); \nB.printf("Hello World"); \nC.Print("HelloWorld");\n D.Print(Hello World);""",
         """A.//Comments\nB./*Comments*/ \nC.#Comments \nD.All the above"""]
    
    corans=['B','A','C']
    playermarks=0
    print("welcom to Quiz App")
    print("------------************---------------")
    for i in range(len(que)):
        print(i+1,'.',end="")
        print(que[i])
        print(ans[i])
        player=str(input("enter your answer:"))
        if player.upper()==corans[i]:
            playermarks+=1
            print("correct")
        else:
            print("wrong")
print("Quiz Completed")
print("your Score is :{0}/{1}".format(playermarks,len(que)))
print("Thank you")
        
         
        
