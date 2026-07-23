class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i :[] for i in range(numCourses)}

        for crs , pre in prerequisites:
            premap[crs].append(pre)
        #create premap for each course crs 1 its prereq are 0,2 (hashmap) 
        #visitset = all courses along curr dfs path save if repeated then loop 
        visit= set()

        def dfs(crs):
            if crs in visit:
                return False
            if premap[crs]==[]: #meanign this course doenst have prereqs
                return True

            visit.add(crs)
            for pre in premap[crs]: #recursively keep calling prereqs 
                if not dfs(pre):
                    return False
            
            visit.remove(crs)
            premap[crs]=[]
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        
        return True

        

        