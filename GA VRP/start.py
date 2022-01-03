from GA import *
from DE import *
def Run_program():
    print("choose the  algorithm(enter the nunber)")
    print("1-Genetic algorithm\n2-Differential evolution")
    choise=int(input())
    if choise==1:
        GA_part()
    elif choise==2:
        main()
    else:
        Run_program()
    return
Run_program()
"""
def main(bounds, popsize, mutate, recombination, maxiter) عرف المتغيرات اللى مكتوبة فى تعريب الدالة دى قبل ما تنديها
"""