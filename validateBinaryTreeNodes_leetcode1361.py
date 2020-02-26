class Solution:
  def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:        
    visited = []
    visited.append(0)
    for i in range(len(leftChild)):
        if(leftChild[i] in visited or rightChild[i] in visited):
            return False
        if (leftChild[i] != -1):
            visited.append(leftChild[i])
        if(rightChild[i] != -1):
            visited.append(rightChild[i])
        if(i not in visited):
            return False

    return True
