from stack import *
def priority(ch):
    if(ch=='^'):
        return 3
    elif(ch=='*' or ch=='/' or ch=='%'):
        return 2
    elif(ch=='+' or ch=='-'):
        return 1
    return 0

def postfixsol(exp):
    st=stack()
    val='0'
    a='0'
    b='0'
    for i in exp.split():
        if(priority(i)==0):
            st.push(int(i))
        else:
            try:
                a=st.top()
                st.pop()
                b=st.top()
                st.pop()
                if(i=='+'):
                    val=a+b
                elif(i=='-'):
                    val=b-a
                elif(i=='*'):
                    val=a*b
                elif(i=='/'):
                    val=b/a
                elif(i=='%'):
                    val=b%a
                elif(i=='^'):
                    val=b**a
                st.push(val)
            except:
                return "!! Invalid Expression !!"
    return st.top()

def solve_expression(exp):
    val=""
    # convert infix to postfix
    st=stack()
    exp+=' '
    i=0
    if(priority(exp[0])==1):
        i=1
        val=exp[0]
    while(i<len(exp)):
        if(exp[i]>='0' and exp[i]<='9'):
            num=""
            while(exp[i]>='0' and exp[i]<='9'):
                num+=exp[i]
                i+=1
            val+=num+' '
            i-=1
        elif(exp[i]=='('):
            st.push(exp[i])
        elif(exp[i]==')'):
            while(st.top()!='('):
                val+=st.top()+' '
                st.pop()
            st.pop()
        else:
            while( st.empty() and priority(exp[i])<=priority(st.top()) ):
                val+=st.top()+' '
                st.pop()
            st.push(exp[i])
        i+=1
    while(not st.empty()):
        val+=st.top()+' '
        st.pop()
    return postfixsol(val)
