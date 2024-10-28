import hashlib

class MerkleNode:
  def __init__(self,left=None,right=None,data=None):
    self.left = left
    self.right = right
    self.data = data

  def compute_hash(self):
    if self.left == None and self.right == None: #If leaf node->compute hash
      return hashlib.sha256(self.data.encode()).hexdigest()
    
    if self.left:
      left_hash = self.left.compute_hash()
    if self.right:
      right_hash = self.right.compute_hash()
    
    return hashlib.sha256((left_hash+right_hash).encode()).hexdigest()
  
class MerkleTree:
  def __init__(self):
    self.root = None
  
  def build_tree(self,file_hashes):
    nodes = [MerkleNode(data=file_hash) for file_hash in file_hashes]
    while len(nodes) > 1:
      temp_nodes = []
      for i in range(0,len(nodes),2):
        left = nodes[i]
        right = nodes[i+1] if (i+1)<len(nodes) else None
        combined_node = MerkleNode(left,right)
        temp_nodes.append(combined_node)
      
      nodes = temp_nodes
    if nodes:
      self.root = nodes[0]
    else:
      self.root = None
  
  def get_root_hash(self):
    if self.root:
      return self.root.compute_hash()
    return None