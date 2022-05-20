import solve;
def test_solve():
    qa_set =[(1,"1/2"), (2,"2/4"), (3,"4/8"), (4,"7/15"), (5,"14/29"), (6,"27/56"), (7,"52/108"), (8,"100/208"), (9,"193/401"), (10,"372/773")]
    for input,solution in qa_set:
        assert solve.solve(input) == solution
        