from python_datastructure import *
import random
import math
import matplotlib.pyplot as plot
import networkx as nx
class entrance:
    def __init__(self,graph):
        self.number_of_driver=None
        self.targets_list=None
        self._graph=graph
    def get_number_of_drivers(self):
        if self.number_of_driver:
            return self.number_of_driver
        else:
            self.number_of_driver=int(input("number of drivers please!!!\n"))
            return self.number_of_driver
    def set_number_of_driver(self,new_drivers):
        self.number_of_driver=new_drivers
    def set_target_list(self,list_of_targets):
        self.targets_list=list_of_targets
    def get_targets_list(self):
        if self.targets_list:
            return self.targets_list
        else:
            self.targets_list=[]
            self.number_of_driver=self.get_number_of_drivers()
            i=0
            while i<self.number_of_driver:
                print("enter all targets for driver ",i+1)
                inp=None
                target=[]
                while True:
                    inp=input("enter the target city code")
                    try:
                        target.append(int(inp))
                    except ValueError:
                        break
                    except AttributeError:
                        break
                self.targets_list.append(target)
                i=i+1
            return self.targets_list
    def _copy_list(self,list_):
        copy=[]
        for item in list_:
            copy.append(item)
        return list_
    def _concat_lists(self,list1,list2):
        list3=[]
        for item in list2:
          list1.append(item)
    def __build_corm(self,driver_number):
        targets=self.targets_list[driver_number]
        list_=targets.copy()
        corm=[]
        i=0
        for item in list_:
            corm_part=[]
            corm_part=self._graph.find_Route(item, list_[i])
            corm=corm+corm_part
            i+=1
        corm_part=self._graph.find_Route(list_.pop(-1), list_.pop(0))
        return corm
    def __build_individual(self):
        indivi={}
        for i in range(self.number_of_driver):
            corm=self.__build_corm(i)
            indivi[i]=corm
        return indivi
    def build_population(self,pop_size):
        pop=[]
        self.targets_list=self.get_targets_list()
        for i in range(pop_size):
            ind=self.__build_individual()
            pop.append(ind)
        return pop
class VRP_GEN:
    #farghly
    def __init__(self,pop,optimal_cost,iterations=50,split_ratio=0.5):
        self._pop=pop
        self._cost=optimal_cost
        self._iter=iterations
        self.split_ratio=split_ratio
        self._cost_iter=[]
    #ahmed emad aldain
    def _calc_single_route(self,route):
        """
            this method take parameter route as follows:
                [[1,14],[4,5],[6,8]]
            and calculate the total cost
        """
        cost=0
        for item in route:
            cost=cost+item[1]
        return cost

    # ahmed emad aldain
    def _calc_single_pop(self,pop_member):
        """
            this function calculate the total cost for single individual
        """
        total_cost=0
        for route in pop_member.values():
            route_cost=self._calc_single_route(route)
            total_cost=total_cost+route_cost
        return total_cost
    #ahmed emad ahmed
    def _modifiy_gen(self,corm):
        corm[1]=abs(corm[1]-0.5)
        return None
    # ahmed emad ahmed
    def _mutate(self,child):
        """
            I see the mutation here is entirly useless in VRP but the genetics must have mutation in the GA 
        """
        for i in range(0,len(child)):
            self._modifiy_gen(child[i][random.randrange(0,len(child[i]))])
        return child
    # ahmed emad ahmed
    def _cross_over(self,individ1,individ2):
        """
            this method take two individuals and do cross over them
        """
        i=0
        child={}
        while i<len(individ1):
            cost_rout1=self._calc_single_route(individ1[i])
            cost_rout2=self._calc_single_route(individ2[i])
            if cost_rout1<cost_rout2:child[i]=individ1[i]
            else:child[i]=individ2[i]
            i=i+1
        total_cost=self._calc_single_pop(child)
        self._cost_iter.append(total_cost)
        return child

    # ahmed emad aldain
    def fittness(self,partition):
        """
            check if the individual is ready for cross over randomly
        """
        individ=partition[random.randrange(0,len(partition))]
        return individ

    # ahmed emad aldain
    def _check_for_fitt(self):
        """
            check if we reached the most optimal solution
        """
        total_cost=0
        i=-1
        for indivi in self._pop:
            i=i+1
            total_cost=self._calc_single_pop(indivi)
            if total_cost<self._cost:
                return i
        return False

    # ahmed emad aldain
    def find_fittest(self):
        for item in self._pop:
            total_cost=self._calc_single_pop(item)
            if total_cost<self._cost:
                return item
        return False
    # ahmed emad aldain
    def _select_fittests(self):
        partition=[]
        #getting the 
        for individ in self._pop:
            individ_cost=self._calc_single_pop(individ)
            if len(partition)>math.ceil((self.split_ratio*len(self._pop))):
                i=0
                while i<len(partition):
                   current=self._calc_single_pop(partition[i])
                   if current>individ_cost:
                       partition.insert(i,individ)
                   i=i+1
                   partition.pop(-1)
                   pass
            else:
                partition.append(individ)
        return partition
    #farghly
    def Run_GA(self):
        i=0
        self._iteration_list=[]
        where_fittest=self._check_for_fitt()
        new_pop=[]
        while i<self._iter and not where_fittest:
            child={}
            partition=self._select_fittests()
            for individ in partition:
                x=self.fittness(partition)
                y=self.fittness(partition)
                child=self._cross_over(x,y)
                child=self._mutate(child)
                new_pop.append(child)
            self._pop=new_pop
            where_fittest=self._check_for_fitt()
            i=i+1
            self._iteration_list.append(i)
        return self._pop
    # farghly
    def get_iterations(self):
        return self._iteration_list
    # farghly
    def get_cost(self):
        return self._cost_iter
    # farghly
    def calculate_cost(self,individ):
        return self._calc_single_pop(individ)
    # farghly
    def Plot_evo(self):
        fig,ax=plot.subplots(figsize=(12,6))
        ax.scatter(self.get_cost(),range(len(self.get_cost())))
        ax.set_xlabel("cost")
        ax.set_ylabel("child's cost in any generation")
        plot.show()
        return None
    # farghly
    def Draw_networkX(self,graph):
        G=nx.Graph()
        vlist=graph.get_graph()
        for k in vlist.keys():
            for edge in vlist[k]:
                G.add_edge(k, edge[0], weight=edge[1])
        return G
    # farghly
    def plot_graph(self,G):
        subox=plot.subplot(121)
        nx.draw(G ,pos=nx.random_layout(G),with_labels=True, font_weight='bold')
        return None
def GA_part():
    entr=entrance(graph)
    entr.get_number_of_drivers()
    entr.get_targets_list()
    pop=entr.build_population(100)
    GA=VRP_GEN(pop,10000)
    pop=GA.Run_GA()
    print("Genetic Algorithm is done")
    print("optimal table:-\n")
    fittest=GA.find_fittest()
    print(fittest)
    print("with cost:-\n",GA.calculate_cost(fittest))
    print(GA.get_iterations())
    GA.plot_graph(GA.Draw_networkX(graph))
