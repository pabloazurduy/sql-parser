import os


from sqlparse import engine 
from sqlparse import filters

def sql_formater(sql:str)-> str:
    stack = engine.FilterStack() 
    stack.enable_grouping() # needed for the stmtprocess filters 
    stack.preprocess.append(filters.KeywordCaseFilter('lower'))  # Transform keywords to lower case  
    stack.preprocess.append(filters.IdentifierCaseFilter('lower'))  # Transform (AS <identifier>) to lower case  
    stack.stmtprocess.append(filters.SpacesAroundOperatorsFilter())
    # stack.stmtprocess.append(filters.StripCommentsFilter()) # remove comments
    stack.stmtprocess.append(filters.ReindentFilter(
                                #width=2,
                                #indent_after_first=True,
                                #indent_columns=True,
                                #wrap_after=,
                                #comma_first=False
                            ))
    stack.stmtprocess.append(filters.AlignedIndentFilter())
    stack.postprocess.append(filters.SerializerUnicode())

    formated_sql = ''.join(stack.run(sql))
    return formated_sql

if __name__=='__main__':
    with open(os.path.join('example', 'input.sql'), 'r') as f:
        input = f.read()
    formatted_sql =  sql_formater(input)
    print(formatted_sql)
    with open(os.path.join('example', 'output.sql'), 'w') as f:
        f.write(formatted_sql)

    
