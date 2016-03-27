"""
CSCI-603 PreTee Lab
Author: Sean Strout @ RIT CS
Author: Vishal Garg

The main program and class for a prefix expression interpreter of the
PreTee language.  See prog1.pre for a full example.

Usage: python3 pretee.py source-file.pre
"""

import sys              # argv
import literal_node     # literal_node.LiteralNode
import variable_node    # variable_node.VariableNode
import assignment_node  # assignment_node.AssignmentNode
import print_node       # print_node.PrintNode
import math_node        # math_node.MathNode
import syntax_error     # syntax_error.SyntaxError
import runtime_error    # runtime_error.RuntimeError

class PreTee:
    """
    The PreTee class consists of:
    :slot srcFile: the name of the source file (string)
    :slot symTbl: the symbol table (dictionary: key=string, value=int)
    :slot parseTrees: a list of the root nodes for valid, non-commented
        line of code
    :slot lineNum:  when parsing, the current line number in the source
        file (int)
    :slot syntaxError: indicates whether a syntax error occurred during
        parsing (bool).  If there is a syntax error, the parse trees will
        not be evaluated
    """
    __slots__ = 'srcFile', 'symTbl', 'parseTrees', 'lineNum', 'syntaxError'

    # the tokens in the language
    COMMENT_TOKEN = '#'
    ASSIGNMENT_TOKEN = '='
    PRINT_TOKEN = '@'
    ADD_TOKEN = '+'
    SUBTRACT_TOKEN = '-'
    MULTIPLY_TOKEN = '*'
    DIVIDE_TOKEN = '//'
    MATH_TOKENS = ADD_TOKEN, SUBTRACT_TOKEN, MULTIPLY_TOKEN, DIVIDE_TOKEN

    def __init__(self, srcFile):
        """
        Initialize the parser.
        :param srcFile: the source file (string)
        """
        self.srcFile=srcFile
        self.parseTrees=[]
        self.symTbl=dict()
        self.lineNum=0
        self.syntaxError=False
        PreTee.count=0

    def __parse(self, tokens):
        """
        The recursive parser that builds the parse tree from one line of
        source code.
        :param tokens: The tokens from the source line separated by whitespace
            in a list of strings.
        :exception: raises a syntax_error.SyntaxError with the message
            'Incomplete statement' if the statement is incomplete (e.g.
            there are no tokens left and this method was called).
        :exception: raises a syntax_error.SyntaxError with the message
            'Invalid token {token}' if an unrecognized token is
            encountered (e.g. not one of the tokens listed above).
        :return:
        """
        PreTee.count+=1
        #Check if we needed more input but it is not there
        if PreTee.count>len(tokens):
            raise syntax_error.SyntaxError("Insufficient arguments")
        #Check if input is a digit(literal_node)
        if tokens[PreTee.count-1].isdigit():
            temp=int(tokens[PreTee.count-1])
            return literal_node.LiteralNode(temp)
        #Check if input is a identifier like x or y
        elif tokens[PreTee.count-1].isidentifier():
            temp=tokens[PreTee.count-1]
            return variable_node.VariableNode(temp,self.symTbl)
        #Check if there is an assignment operation
        elif tokens[PreTee.count-1] is PreTee.ASSIGNMENT_TOKEN:
            tokenEqual=tokens[PreTee.count-1]
            if len(tokens[PreTee.count-1:])<3:
                raise syntax_error.SyntaxError("Incomplete statement")
            temp=self.__parse(tokens)
            if not isinstance(temp,variable_node.VariableNode):
                raise syntax_error.SyntaxError("Bad assignment to non-variable")
            var2=self.__parse(tokens)
            if not isinstance(var2,(variable_node.VariableNode,literal_node.LiteralNode,math_node.MathNode)):
                raise syntax_error.SyntaxError("Bad assignment expression")
            return assignment_node.AssignmentNode(temp,var2,self.symTbl,tokenEqual)
        #Check if print operation was asked for
        elif tokens[PreTee.count-1] is PreTee.PRINT_TOKEN:
            if len(tokens[PreTee.count-1:])>1:
                return print_node.PrintNode(self.__parse(tokens))
            else:
                return print_node.PrintNode(None)
        #Check if a math node has to be created
        elif tokens[PreTee.count-1] in PreTee.MATH_TOKENS:
            tokenEval=tokens[PreTee.count-1]
            left=self.__parse(tokens)
            right=self.__parse(tokens)
            return math_node.MathNode(left,right,tokenEval)
        #Check if input is a comment
        elif tokens[PreTee.count-1] in PreTee.COMMENT_TOKEN:
             pass
        else:
            err="Invalid token '" + tokens[PreTee.count-1] +"'"
            raise syntax_error.SyntaxError(err)

    def parse(self):
        """
        The public parse is responsible for looping over the lines of
        source code and constructing the parseTree, as a series of
        calls to the helper function that are appended to this list.
        It needs to handle and display any syntax_error.SyntaxError
        exceptions that get raised.
        : return None
        """
        with open(self.srcFile) as file:
            for line in file:
                self.lineNum+=1
                try:
                    PreTee.count=0
                    list=line.split()
                    if len(list)>0:
                        self.parseTrees.append(self.__parse(list))
                except syntax_error.SyntaxError as e:
                    self.syntaxError=True
                    print("Syntax Error:", e ,":Line Number", str(self.lineNum))
        if self.syntaxError:
            print("\nFound syntax errors: Not executing further")
            exit(1)

    def emit(self):
        """
        Prints an infiex string representation of the source code that
        is contained as root nodes in parseTree.
        :return None
        """
        for node in self.parseTrees:
            if node is not None:
                print(node.emit())

    def evaluate(self):
        """
        Prints the results of evaluating the root notes in parseTree.
        This can be viewed as executing the compiled code.  If a
        runtime error happens, execution halts.
        :exception: runtime_error.RunTimeError may be raised if a
            parse tree encounters a runtime error
        :return None
        """
        for node in self.parseTrees:
            if node is not None:
                temp=node.evaluate()
                if temp is not None:
                    print(node.evaluate())

def main():
    """
    The main function prompts for the source file, and then does:
        1. Compiles the prefix source code into parse trees
        2. Prints the source code as infix
        3. Executes the compiled code
    :return: None
    """
    if len(sys.argv) != 2:
        print('Usage: python3 pretee.py source-file.pre')
        return

    pretee = PreTee(sys.argv[1])
    print('PRETEE: Compiling', sys.argv[1] + '...')
    pretee.parse()
    print('\nPRETEE: Infix source...')
    pretee.emit()
    print('\nPRETEE: Executing...')
    try:
        pretee.evaluate()
    except runtime_error.RuntimeError as e:
        # on first runtime error, the supplied program will halt execution
        print('*** Runtime error:', e)

if __name__ == '__main__':
    main()