import tensorflow as tf
print(tf.version)



# each tensor represnts a partialy defined computation that will eventually produce a value.
# creating tensors:
string = tf.Variable("this is a string", tf.string)
number = tf.variable(324, tf.int16)
floating = tf.Variale("3.567, tf.float64")

# rank/degree of tensors
# simply mean the numer of dimentions involved in the tensor
rank1_tensor = t.Variable(["Test"], tf.string)
rank1_tensor = t.Variable([["test", "ok"], ["test", "yes"]], tf.string)
# to determine the rank of a tensor:
tf.rank(rank2_tensor)

# shape of a tensor
# the amount o elements that exists in each dimention.
rank2_tensor.shape      # [2, 2]
# changing shape
tensor1 = tf.ones([1,2,3])              # tf.ones() creates a shape [1,2,3] tensor full o ones
tensor2 = tf.reshape(tensor1, [2,3,1])  # reshape existing data to shape [2,3,1]
tensor3 = tf.reshape(tensor2, [3, -1])  # -1 tells the tensor to calculate the size of the dimention in that place
                                        # this will reshape the tensor to [3,2]

# types of tensors:
Variable, Constant, Placeholder, SparseTensor
# With the exception of "Variable" all of these tensors are immuttable, meaning their value may not change during execcution


# evaluating tenors
# in other words, get its value
# Since tensors represnts a partially cmplete computation we will sometimes need to run a "session" to evaluate the tensor
with tf.Session() as sess:      # create a session using the default graph
    tensor.eval()               # tensor will of course be the name of your tensor
# In the code above we evalated the tenor variable that was stored in the default graph.
# The default graph holds all operations not specified to any other graph

