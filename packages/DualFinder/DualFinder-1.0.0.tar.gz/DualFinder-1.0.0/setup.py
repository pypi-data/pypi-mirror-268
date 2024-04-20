import setuptools

setuptools.setup(
     name="DualFinder",
     version="1.0.0",
     author="Isaac Moskowitz",
     author_email="isaac.moskowitz@yale.edu",
     description="A trainable and visualizable convolutional neural network designed to detect galaxy and AGN mergers. ",
     packages=["dual_finder", "dual_finder/preprocess_data", "dual_finder/cnn", "dual_finder/visualize", "dual_finder/optimize"],
     python_requires='>=3.8',
     install_requires=["numpy", "tensorflow >= 2.14", "scipy", "astropy", "scikit-learn", "optuna", "matplotlib", "streamlit"]
     
)
