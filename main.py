from fastmcp import FastMCP
import random

mcp = FastMCP(name="Simple calculator")

@mcp.tool
def add_numbers(a:float,b:float)->float:
    """Returning the sum of two numbers having two arguments a and b"""
    return a+b

@mcp.tool
def generate_random_number(minimum:int = 1,maximum:int = 100):
    """Generating a random number bw 1 and 100"""
    return random.randint(minimum,maximum)

if __name__ == "__main__":
    mcp.run(transport="http",host='0.0.0.0',port=8080)