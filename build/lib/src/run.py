import sys
import time
import ast
from src.vython_parser import Parser
from src.transpiler import Transpiler

def main():
    file_path = "test/sample.py"
    with open(file_path, "r") as file:
        code = file.read()

    compare_file_path = "test/sample_py.py"
    with open(compare_file_path, "r") as file:
        compare_code = file.read()
    
    # Vython ASTをLarkで作成したParserを用いて生成        
    vythonTree = Parser(debug_mode = False).parse(code)

    # 生成したVython ASTをPython ASTに変換
    pythonTree = Transpiler(debug_mode = False).transform(vythonTree)

    # Python ASTをPythonプログラムにUnparse
    pythonProgram = ast.unparse(pythonTree)

    # 結果をtmp.logに表示
    with open('tmp.log', 'w') as log:
        print("[Vython AST]",file=log)
        print(vythonTree,file=log)
        print("",file=log)

        print("[Python AST]",file=log)
        print(ast.dump(pythonTree,False,indent=4),file=log)
        print("",file=log)

        # print("[Python AST-compare]",file=log)
        # print(ast.dump(ast.parse(compare_code),False,True,indent=4),file=log)
        # print("",file=log)

        print("[Unparse Python AST]",file=log)
        print(pythonProgram,file=log)
        print("",file=log)
        

