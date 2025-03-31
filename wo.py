def canCross(tiles):
   
    tile_positions = set(tiles)
    
    
    visited = set()
    
    def dfs(position, last_jump):
       
        if position == tiles[-1]:
            return True
        if position not in tile_positions:
            return False
        
       
        state = (position, last_jump)
        if state in visited:
            return False
        visited.add(state)
        
       
        for next_jump in [last_jump-1, last_jump, last_jump+1]:
            if next_jump > 0:  
                next_pos = position + next_jump
                if dfs(next_pos, next_jump):
                    return True
        
        return False
    
    
    return dfs(0, 0)

tiles = eval(input().strip()) 
print(canCross(tiles))