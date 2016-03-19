import random
import matplotlib.pyplot as plt

def sample_gamma(alpha, beta):
    """
    Sample gamma variate for small alpha, using
    transformation from Marsaglia&Tsang method
    
    http://www.hongliangjie.com/2012/12/19/how-to-generate-gamma-random-variables/
    """
    
    x = random.gammavariate(alpha + 1.0, beta)
    
    return x * pow( random.random(), 1.0/alpha )

if __name__ == "__main__":
    alpha = 0.0001
    bins = [0.0001 * i for i in range(12)]
    q = [sample_gamma(alpha, 1.0) for k in range(10000)]
    print(q)
    plt.hist(q, bins)
    plt.show()
    
