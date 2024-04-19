__name__ = 'sctreeshap'
__version__ = "0.7.6.2"
headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

import time
import threading
import numpy as np
import anndata as ad
import pandas as pd

def checkUpdates():
    import requests
    try:
        url = "https://pypi.org/project/sctreeshap/"
        resp = requests.get(url, headers, timeout=3)
        resp.encoding = 'UTF-8'
        if resp.status_code == 200:
            resp = str(resp.text)
            locate = resp.find('<h1 class="package-header__name">')
            if locate != -1:
                Write = False
                latest_version = ""
                for i in range(locate + 1, len(resp)):
                    if resp[i] == '<':
                        break
                    if Write and resp[i] != '\n':
                        latest_version += resp[i]
                    if resp[i] == '>':
                        Write = True
                latest_version = latest_version.strip()
                if latest_version != __name__ + " " + __version__:
                    print("\033[1;33;40mWarning:\033[0m new version " + latest_version + " available (Currently " + __version__ + "). See updates at https://pypi.org/project/sctreeshap/")
                else:
                    return None
            else:
                print("\033[1;33;40mWarning:\033[0m unable to detect latest version info.")
        else:
            print("\033[1;33;40mWarning:\033[0m unable to detect latest version info.")
    except KeyboardInterrupt:
        raise
    except:
        print("\033[1;33;40mWarning:\033[0m unable to detect latest version info.")
    print('To disable version check, run "sctreeshap.muteNotifications()". To revert, run "sctreeshap.enableNotifications()".')

def download(url, path):
    from tqdm import tqdm
    from urllib.request import urlopen, Request
    blocksize = 1024 * 8
    blocknum = 0
    retry_times = 0
    while True:
        try:
            with urlopen(Request(url, headers=headers), timeout=3) as resp:
                total = resp.info().get("content-length", None)
                with tqdm(
                    unit="B",
                    unit_scale=True,
                    miniters=1,
                    unit_divisor=1024,
                    total=total if total is None else int(total),
                ) as t, path.open("wb") as f:
                    block = resp.read(blocksize)
                    while block:
                        f.write(block)
                        blocknum += 1
                        t.update(len(block))
                        block = resp.read(blocksize)
            break
        except KeyboardInterrupt:
            if path.is_file():
                path.unlink()
            raise
        except:
            retry_times += 1
            if retry_times >= 20:
                break
            print("Timed out, retrying...")
    if retry_times >= 20:
        if path.is_file():
            path.unlink()
        raise ConnectionError("bad internet connection, check it and retry.")

def clearDownload():
    import os
    data_directory = __file__[:-13] + "sctreeshap_data"
    if os.path.exists(data_directory):
        tmp = data_directory + "/tmp"
        if os.path.exists(tmp):
            target_files = [("INPUT_DATA.h5ad.tar.bz2.part" + (3 - len(str(i))) * '0' + str(i)) for i in range(1, 43)]
            for files in os.listdir(tmp):
                if str(files) in target_files:
                    os.remove(os.path.join(tmp, files))
            if len(os.listdir(tmp)) == 0:
                os.rmdir(tmp)
        if os.path.isfile(os.path.join(data_directory, "INPUT_DATA.h5ad.tar.bz2")):
            os.remove(os.path.join(data_directory, "INPUT_DATA.h5ad.tar.bz2"))
        if os.path.isfile(os.path.join(data_directory, "INPUT_DATA.h5ad")):
            os.remove(os.path.join(data_directory, "INPUT_DATA.h5ad"))
        if os.path.isfile(os.path.join(data_directory, "Housekeeping_GenesHuman.csv")):
            os.remove(os.path.join(data_directory, "Housekeeping_GenesHuman.csv"))
        if os.path.isfile(os.path.join(data_directory, "Housekeeping_GenesMouse.csv")):
            os.remove(os.path.join(data_directory, "Housekeeping_GenesMouse.csv"))
        if len(os.listdir(data_directory)) == 0:
            os.rmdir(data_directory)

def muteNotifications():
    file = open(__file__, "r", encoding='utf-8')
    codes = file.readlines()
    codes[len(codes) - 1] = "# " + codes[len(codes) - 1]
    file.close()
    file = open(__file__, "w", encoding='utf-8')
    file.writelines(codes)

def enableNotifications():
    file = open(__file__, "r", encoding='utf-8')
    codes = file.readlines()
    codes[len(codes) - 1] = "checkUpdates()"
    file.close()
    file = open(__file__, "w", encoding='utf-8')
    file.writelines(codes)

def upgrade():
    from pip._internal import main
    main(['install', '--upgrade', 'sctreeshap'])

def uninstall():
    clearDownload()
    from pip._internal import main
    main(['uninstall', 'sctreeshap'])

class sctreeshap:
    def __showProcess(self):
        print(self.__waitingMessage, end="  ")
        while self.__isFinished is False:
            print('\b-', end='')
            time.sleep(0.05)
            print('\b\\', end='')
            time.sleep(0.05)
            print('\b|', end='')
            time.sleep(0.05)
            print('\b/', end='')
            time.sleep(0.05)
        if self.__isFinished is True:
            print('\bdone')
        else:
            print('\berror!')

    def __checkLoops(self, root):
        checkResult = True
        self.__visited.append(root)
        if root not in self.__TreeNode:
            return True
        for item in self.__TreeNode[root]:
            if item in self.__visited:
                return False
            else:
                checkResult = self.__checkLoops(item)
        return checkResult

    def __buildClusterTree(self, tree_arr):
        if not isinstance(tree_arr, dict):
            raise TypeError("in method 'sctreeshap.sctreeshap()' (in file '" + __file__ + "'), parameter 'tree_arr' receives " + str(type(tree_arr)) + ", expected <class 'dict'>.")
        typeOfTree = None
        for key in tree_arr.keys():
            if not isinstance(tree_arr[key], list) and not isinstance(tree_arr[key], tuple):
                raise ValueError("in method 'sctreeshap.sctreeshap()' (in file '" + __file__ + "'), parameter 'tree_arr' receives an invalid dict (wrong format).")
            if typeOfTree is None:
                if len(tree_arr[key]) > 1 and isinstance(tree_arr[key][1], int):
                    typeOfTree = "ParentPointer"
                else:
                    typeOfTree = "ChildPointer"
            else:
                if len(tree_arr[key]) > 1 and isinstance(tree_arr[key][1], int):
                    if typeOfTree == "ChildPointer":
                        raise ValueError("in method 'sctreeshap.sctreeshap()' (in file '" + __file__ + "'), parameter 'tree_arr' receives an invalid dict (wrong format).")
                else:
                    if typeOfTree == "ParentPointer":
                        raise ValueError("in method 'sctreeshap.sctreeshap()' (in file '" + __file__ + "'), parameter 'tree_arr' receives an invalid dict (wrong format).")
        if typeOfTree == "ChildPointer":
            self.__TreeNode = tree_arr
            for key in tree_arr.keys():
                for item in tree_arr[key]:
                    if item not in self.__parent.keys():
                        self.__parent[item] = key
                    else:
                        raise ValueError("in method 'sctreeshap.sctreeshap()' (in file '" + __file__ + "'), parameter 'tree_arr' receives an invalid dict (not a tree structure).")
            for key in tree_arr.keys():
                if key not in self.__parent.keys():
                    if self.__root is None:
                        self.__root = key
                    else:
                        raise ValueError("in method 'sctreeshap.sctreeshap()' (in file '" + __file__ + "'), parameter 'tree_arr' receives an invalid dict (not a tree structure).")
            if self.__root is None:
                raise ValueError("in method 'sctreeshap.sctreeshap()' (in file '" + __file__ + "'), parameter 'tree_arr' receives an invalid dict (not a tree structure).")
            if not self.__checkLoops(self.__root):
                raise ValueError("in method 'sctreeshap.sctreeshap()' (in file '" + __file__ + "'), parameter 'tree_arr' receives an invalid dict (not a tree structure).")
        else:
            # needs implementation
            raise Exception("in method 'sctreeshap.sctreeshap()' (in file '" + __file__ + "'), parameter 'tree_arr' receives a valid but not yet supported format. Please contact the developer.")
        return True

    # Construct a sctreeshap object with a given cluster tree.
    # tree_arr: dictionary, can be in 2 different formats:
    #           1. Let n <- len(tree_arr);
    #                   then n represents the number of non-leaf nodes in the cluster tree;
    #               tree_arr[str] represents the node of name str in the cluster tree;
    #                   tree_arr[str] can be a list or a tuple of strings, representing the name of childs of the node (from left to right);
    #                   e.g. tree_arr['n1'] = ('n2', 'n70') represents a node named 'n1', whose left child is 'n2' and right child is 'n70';
    #               note that you do not need to create nodes for clusters, since they are leaf nodes and have no childs.
    #            2. Let n <- len(tree_arr);
    #                   then n represents the number of nodes (root excluded) in the cluster tree;
    #               tree_arr[str] represents the node of name str in the cluster tree;
    #                   tree_arr[str] should be a list or a tuple of a string and an int, representing the name of parent of the node and which child it is (from left to right, start from 0);
    #                   e.g. tree_arr['n2'] = ('n1', 0) represents a node named 'n2', who is the leftmost child of 'n1';
    #               note that you do not need to create a node for the root, since it does not have a parent.
    # If tree_arr is None, then it does not construct a cluster tree.
    def __init__(self, tree_arr=None):
        self.numOfClusters = 0
        self.clusterDict = {}
        self.__dataDirectory = None
        self.__dataSet = None
        self.__branch = None
        self.__cluster = None
        self.__clusterSet = []
        self.__waitingMessage = None
        self.__isFinished = False
        self.__model = None
        self.__explainer = None
        self.__shapValues = None
        self.__maxDisplay = None
        self.__featureNames = None
        self.__TreeNode = None
        self.__parent = {}
        self.__root = None
        self.__visited = []
        self.__shapParamsBinary = {
            "max_display": 10,
            "model_output": 'raw',
            "bar_plot": True,
            "beeswarm": True,
            "force_plot": False,
            "heat_map": False,
            "decision_plot": False
        }
        self.__shapParamsMulti = {
            "max_display": 10,
            "model_output": 'raw',
            "bar_plot": True,
            "beeswarm": False,
            "decision_plot": False
        }
        if tree_arr is None:
            return None
        self.__buildClusterTree(tree_arr)

    # Set default data directory.
    # data_directory: a string representing the directory of the default input file.
    def setDataDirectory(self, data_directory=None):
        if data_directory is None:
            self.__dataDirectory = None
            return None
        if not isinstance(data_directory, str):
            raise TypeError("in method 'sctreeshap.sctreeshap.setDataDirectory()' (in file '" + __file__ + "'), parameter 'data_directory' receives " + str(type(data_directory)) + ", expected <class 'str'>.")
        self.__dataDirectory = data_directory
        return None
    
    # Set default dataset.
    # data: DataFrame or AnnData.
    def setDataSet(self, data=None):
        if data is None:
            self.__dataSet = None
            return None
        if not isinstance(data, pd.core.frame.DataFrame) and not isinstance(data, ad._core.anndata.AnnData):
            raise TypeError("in method 'sctreeshap.sctreeshap.setDataSet()' (in file '" + __file__ + "'), parameter 'data' receives " + str(type(data)) + ", expected <class 'pandas.core.frame.DataFrame'> or <class 'anndata._core.anndata.AnnData'>.")
        self.__dataSet = data
        return None
    
    # Set default feature names.
    # feature_names: ndarray, list or tuple.
    def setFeatureNames(self, feature_names=None):
        if feature_names is None:
            self.__featureNames = None
            return None
        if not isinstance(feature_names, np.ndarray) and not isinstance(feature_names, list) and not isinstance(feature_names, tuple):
            raise TypeError("in method 'sctreeshap.sctreeshap.setFeatureNames()' (in file '" + __file__ + "'), parameter 'feature_names' receives " + str(type(feature_names)) + ", expected <class 'numpy.ndarray'>, <class 'list'> or <class 'tuple'>.")
        self.__featureNames = np.array(feature_names)
        return None
    
    # Set default branch.
    # branch_name: str, representing the branch's name, which would be defaultedly chosen.
    def setBranch(self, branch_name=None):
        if branch_name is None:
            self.__branch = None
            return None
        if not isinstance(branch_name, str):
            raise TypeError("in method 'sctreeshap.sctreeshap.setBranch()' (in file '" + __file__ + "'), parameter 'branch_name' receives " + str(type(branch_name)) + ", expected <class 'str'>.")
        self.__branch = branch_name
        return None
    
    # Set default cluster.
    # cluster_name: str, representing the cluster's name, which would be defaultedly chosen.
    def setCluster(self, cluster_name=None):
        if cluster_name is None:
            self.__cluster = None
            return None
        if not isinstance(cluster_name, str):
            raise TypeError("in method 'sctreeshap.sctreeshap.setCluster()' (in file '" + __file__ + "'), parameter 'cluster_name' receives " + str(type(cluster_name)) + ", expected <class 'str'>.")
        self.__cluster = cluster_name
        return None
    
    # Set default target cluster set.
    # cluster_set: a list or tuple of strings containing all target clusters to choose.
    def setClusterSet(self, cluster_set=None):
        if cluster_set is None:
            self.__clusterSet = None
            return None
        if not isinstance(cluster_set, np.ndarray) or not isinstance(cluster_set, list) and not isinstance(cluster_set, tuple):
            raise TypeError("in method 'sctreeshap.sctreeshap.setClusterSet()' (in file '" + __file__ + "'), parameter 'cluster_set' receives " + str(type(cluster_set)) + ", expected <class 'numpy.ndarray'>, <class 'list'> or <class 'list'>.")
        self.__clusterSet = tuple(cluster_set)
        return None
    
    # Set default shap plots parameters of explainBinary().
    # shap_params: dictionary, including five keys: ["max_display", "bar_plot", "beeswarm", "force_plot", "heat_map", "decision_plot"], which is defaultedly set as [10, True, True, False, False, False];
    #           you can reset the dict to determine what kinds of figures to output, and maximum number of genes you want to depict.
    def setShapParamsBinary(self, shap_params=None):
        if shap_params is None:
            self.__shapParamsBinary = {
                "max_display": 10,
                "model_output": 'raw',
                "bar_plot": True,
                "beeswarm": True,
                "force_plot": False,
                "heat_map": False,
                "decision_plot": False
            }
            return None
        if not isinstance(shap_params, dict):
            raise TypeError("in method 'sctreeshap.sctreeshap.setShapParamsBinary()' (in file '" + __file__ + "'), parameter 'shap_params' receives " + str(type(shap_params)) + ", expected <class 'dict'>.")
        self.__shapParamsBinary = shap_params
        return None
    
    # Set default shap plots parameters of explainMulti().
    # shap_params: dictionary, including three keys: ["max_display", "bar_plot", "beeswarm", "decision_plot"], which is defaultedly set as [10, True, False, False];
    #           you can reset the dict to determine what kinds of figures to output, and maximum number of genes you want to depict.
    def setShapParamsMulti(self, shap_params=None):
        if shap_params is None:
            self.__shapParamsMulti = {
                "max_display": 10,
                "model_output": 'raw',
                "bar_plot": True,
                "beeswarm": False,
                "decision_plot": False
            }
            return None
        if not isinstance(shap_params, dict):
            raise TypeError("in method 'sctreeshap.sctreeshap.setShapParamsMulti()' (in file '" + __file__ + "'), parameter 'shap_params' receives " + str(type(shap_params)) + ", expected <class 'dict'>.")
        self.__shapParamsMulti = shap_params
        return None

    # Get XGBClassifier of the last job (available after 'a.explainBinary()' or 'a.explainMulti()').
    # Return: <class 'xgboost.sklearn.XGBClassifier'> object
    def getClassifier(self):
        return self.__model

    # Get shap explainer of the last job (available after 'a.explainBinary()' or 'a.explainMulti()').
    # Return: <class 'shap.explainers._tree.Tree'> object
    def getExplainer(self):
        return self.__explainer
    
    # Get shap values of the last job (available after 'a.explainBinary()' or 'a.explainMulti()').
    # Return: ndarray.
    def getShapValues(self):
        return self.__shapValues
    
    # Get top genes of max absolute mean shap values.
    # max_display: int, the number of top genes you want to derive.
    # shap_values: list or ndarray.
    # feature_names: ndarray, list or tuple.
    # Return: ndarray.
    def getTopGenes(self, max_display=None, shap_values=None, feature_names=None):
        if shap_values is None:
            shap_values = self.__shapValues
        if feature_names is None:
            feature_names = self.__featureNames
        if not isinstance(feature_names, np.ndarray) and not isinstance(feature_names, list) and not isinstance(feature_names, tuple):
            raise TypeError("in method 'sctreeshap.sctreeshap.getTopGenes()' (in file '" + __file__ + "'), parameter 'feature_names' receives " + str(type(feature_names)) + ", expected <class 'numpy.ndarray'>, <class 'list'> or <class 'list'>.")
        if not isinstance(max_display, int):
            max_display = self.__maxDisplay
        if isinstance(shap_values, list):
            # Multi-classification
            if shap_values[0].shape[1] != len(feature_names):
                raise ValueError("in method 'sctreeshap.sctreeshap.getTopGenes()' (in file '" + __file__ + "'), found unmatched parameters 'shap_values' and 'feature_names'!")
            max_display = min(max_display, len(feature_names))
            feature_order = np.argsort(np.sum(np.mean(np.abs(shap_values), axis=1), axis=0))
            feature_order = feature_order[-min(max_display, len(feature_order)):][::-1]
            feature_names = [feature_names[i] for i in feature_order]
            return np.array(feature_names)
        elif isinstance(shap_values, np.ndarray):
            # Binary classification
            if shap_values.shape[1] != len(feature_names):
                raise ValueError("in method 'sctreeshap.sctreeshap.getTopGenes()' (in file '" + __file__ + "'), found unmatched parameters 'shap_values' and 'feature_names'!")
            max_display = min(max_display, len(feature_names))
            feature_order = np.argsort(np.sum(np.abs(shap_values), axis=0))
            feature_order = feature_order[-min(max_display, len(feature_order)):][::-1]
            feature_names = [feature_names[i] for i in feature_order]
            return np.array(feature_names)
        else:
            raise TypeError("in method 'sctreeshap.sctreeshap.getTopGenes()' (in file '" + __file__ + "'), parameter 'shap_values' receives " + str(type(shap_values)) + ", expected <class 'numpy.ndarray'> or <class 'list'>.")

    # Find which branch a given cluster is in.
    # cluster_name: str, representing the cluster's name, e.g. "Exc L5-6 THEMIS FGF10".
    #           if cluster_name is None: choose default cluster.
    # Return: str, representing the path.
    def findCluster(self, cluster_name=None, root=None, path="ROOT"):
        if root is None:
            root = self.__root
        if root is None:
            raise Exception("in method 'sctreeshap.sctreeshap.findCluster()' (in file '" + __file__ + "'), found an empty cluster tree!")
        if cluster_name is None:
            cluster_name = self.__cluster
            if cluster_name is None:
                raise ValueError("in method 'sctreeshap.sctreeshap.findCluster()' (in file '" + __file__ + "'), parameter 'cluster_name' not found.")
        if root not in self.__TreeNode.keys():
            return "Cluster " + cluster_name + " not found!"
        childs = self.__TreeNode[root]
        for item in childs:
            if item == cluster_name:
                return path + " --> " + root + " --> " + cluster_name
            else:
                result = self.findCluster(cluster_name, item, path + " --> " + root)
                if result != "Cluster " + cluster_name + " not found!":
                    return result
        return "Cluster " + cluster_name + " not found!"
    
    # List the clusters of a given branch.
    # branch_name: str, representing the branch's name, e.g. "n48".
    #           if branch_name is None: choose default branch; if default is still None, list all clusters.
    # Return: list, including all cluster names under the branch.
    def listBranch(self, branch_name=None):
        if self.__root is None:
            raise Exception("in method 'sctreeshap.sctreeshap.listBranch()' (in file '" + __file__ + "'), found an empty cluster tree!")
        if branch_name is None:
            branch_name = self.__branch
        try:
            if branch_name is None:
                root = self.__root
            else:
                root = self.__TreeNode[branch_name]
        except:
            return [branch_name]
        result = []
        for item in root:
            result = result + self.listBranch(item)
        return result

    # Load default dataset and build default cluster tree.
    # Return: AnnData, the default dataset.
    def loadDefault(self):
        import os
        data_directory = __file__[:-13] + "sctreeshap_data/"
        if not os.path.exists(data_directory) or not os.path.isfile(data_directory + "INPUT_DATA.h5ad"):
            print("First time loading. Downloading the partitioned dataset... (427.6 MiB)")
            if not os.path.exists(data_directory):
                os.mkdir(data_directory)
            import tarfile
            from pathlib2 import Path
            if not os.path.exists(data_directory + "tmp"):
                os.mkdir(data_directory + "tmp")
            for i in range(1, 43):
                part_num = str(i)
                part_num = (3 - len(part_num)) * '0' + part_num
                if os.path.isfile(data_directory + "tmp/INPUT_DATA.h5ad.tar.bz2.part" + part_num):
                    print("Part " + part_num + " has been downloaded. Skipped.")
                    continue
                else:
                    print("Downloading: " + part_num + "/042")
                path = Path(data_directory + "tmp/INPUT_DATA.h5ad.tar.bz2.part" + part_num)
                url = "https://raw.githubusercontent.com/ForwardStar/sctreeshap/main/datasets/INPUT_DATA.h5ad.tar.bz2.part" + part_num
                download(url, path)
            
            print("Downloading finished, files checking...")
            missing_files = []
            for i in range(1, 43):
                part_num = str(i)
                part_num = (3 - len(part_num)) * '0' + part_num
                if not os.path.isfile(data_directory + "tmp/INPUT_DATA.h5ad.tar.bz2.part" + part_num):
                    missing_files.append("INPUT_DATA.h5ad.tar.bz2.part" + part_num)
            if len(missing_files) > 0:
                print("Files", missing_files, "missing! Trying to automatically fix it.")
                for files in missing_files:
                    print("Downloading file " + files + "...")
                    path = Path(data_directory + "tmp/" + files)
                    url = "https://raw.githubusercontent.com/ForwardStar/sctreeshap/main/datasets/" + files
                    download(url, path)
                    
            self.__waitingMessage = "Merging the partitioned dataset..."
            self.__isFinished = False
            thread_merge = threading.Thread(target=self.__showProcess)
            thread_merge.start()
            try:
                path = Path(data_directory + "tmp/")
                outfile = open(os.path.join(data_directory, "INPUT_DATA.h5ad.tar.bz2"), 'wb')
                files = os.listdir(path)
                files.sort()
                for file in files:
                    filepath = os.path.join(path, file)
                    infile = open(filepath, 'rb')
                    data = infile.read()
                    outfile.write(data)
                    infile.close()
                outfile.close()
                self.__isFinished = True
                thread_merge.join()
                time.sleep(0.2)
            except KeyboardInterrupt:
                self.__isFinished = "Error"
                thread_merge.join()
                raise
            except:
                self.__isFinished = "Error"
                thread_merge.join()
                print("\033[1;31;40mError:\033[0m An error occurred during extracting the dataset. The compressed file may be broken. Do you want to redownload it? [y/n] ", end='')
                redownload = input()
                while redownload != 'y' and redownload != 'n':
                    print("\033[1;31;40mError:\033[0m An error occurred during extracting the dataset. The compressed file may be broken. Do you want to redownload it? [y/n] ", end='')
                    redownload = input()
                if redownload == 'y':
                    self.clearDownload()
                    return self.loadDefault()
                raise

            self.__waitingMessage = "Extracting the dataset... (5.9 GiB)"
            self.__isFinished = False
            thread_extract = threading.Thread(target=self.__showProcess)
            thread_extract.start()
            try:
                archive = tarfile.open(os.path.join(data_directory, "INPUT_DATA.h5ad.tar.bz2"), "r:bz2")
                archive.extractall(data_directory)
                archive.close()
            except KeyboardInterrupt:
                self.__isFinished = "Error"
                thread_extract.join()
                raise
            except:
                self.__isFinished = "Error"
                thread_extract.join()
                print("\033[1;31;40mError:\033[0m An error occurred during extracting the dataset. The compressed file may be broken. Do you want to redownload it? [y/n] ", end='')
                redownload = input()
                while redownload != 'y' and redownload != 'n':
                    print("\033[1;31;40mError:\033[0m An error occurred during extracting the dataset. The compressed file may be broken. Do you want to redownload it? [y/n] ", end='')
                    redownload = input()
                if redownload == 'y':
                    self.clearDownload()
                    return self.loadDefault()
                raise
            self.__isFinished = True
            thread_extract.join()
            time.sleep(0.2)

        self.__waitingMessage = "Building default cluster tree..."
        self.__isFinished = False
        thread_build = threading.Thread(target=self.__showProcess)
        thread_build.start()
        tree_arr = {
            "n1": ('n2', 'n70'),
            "n2": ('n26', 'n3'),
            "n3": ('n4', 'n21'),
            "n4": ('n7', 'n5'),
            "n5": ('Exc L5-6 THEMIS DCSTAMP', 'n6'),
            "n6": ('Exc L5-6 THEMIS CRABP1', 'Exc L5-6 THEMIS FGF10'),
            "n7": ('n8', 'Exc L4-5 FEZF2 SCN4B'),
            "n8": ('n9', 'n12'),
            "n9": ('n10', 'Exc L5-6 THEMIS C1QL3'),
            "n10": ('n11', 'Exc L2-3 LINC00507 FREM3'),
            "n11": ('Exc L2 LAMP5 LTK', 'Exc L2-4 LINC00507 GLP2R'),
            "n12": ('n13', 'n17'),
            "n13": ('Exc L3-4 RORB CARM1P1', 'n14'),
            "n14": ('Exc L3-5 RORB ESR1', 'n15'),
            "n15": ('Exc L3-5 RORB COL22A1', 'n16'),
            "n16": ('Exc L3-5 RORB FILIP1L', 'Exc L3-5 RORB TWIST2'),
            "n17": ('n19', 'n18'),
            "n18": ('Exc L5-6 RORB TTC12', 'Exc L4-6 RORB C1R'),
            "n19": ('Exc L4-5 RORB FOLH1B', 'n20'),
            "n20": ('Exc L4-6 RORB SEMA3E', 'Exc L4-5 RORB DAPK2'),
            "n21": ('Exc L4-6 FEZF2 IL26', 'n22'),
            "n22": ('Exc L5-6 FEZF2 ABO', 'n23'),
            "n23": ('n24', 'Exc L5-6 FEZF2 EFTUD1P1'),
            "n24": ('n25', 'Exc L6 FEZF2 OR2T8'),
            "n25": ('Exc L6 FEZF2 SCUBE1', 'Exc L5-6 SLC17A7 IL15'),
            "n26": ('n27', 'n53'),
            "n27": ('n48', 'n28'),
            "n28": ('n41', 'n29'),
            "n29": ('n37', 'n30'),
            "n30": ('n31', 'n34'),
            "n31": ('n32', 'Inh L1-3 VIP GGH'),
            "n32": ('n33', 'Inh L1-3 VIP CCDC184'),
            "n33": ('Inh L1-3 VIP CHRM2', 'Inh L2-4 VIP CBLN1'),
            "n34": ('n36', 'n35'),
            "n35": ('Inh L2-4 VIP SPAG17', 'Inh L1-4 VIP OPRM1'),
            "n36": ('Inh L1-2 VIP LBH', 'Inh L2-3 VIP CASC6'),
            "n37": ('n39', 'n38'),
            "n38": ('Inh L2-5 VIP SERPINF1', 'Inh L2-5 VIP TYR'),
            "n39": ('n40', 'Inh L1-2 VIP PCDH20'),
            "n40": ('Inh L2-6 VIP QPCT', 'Inh L3-6 VIP HS3ST3A1'),
            "n41": ('n43', 'n42'),
            "n42": ('Inh L1-3 VIP ADAMTSL1', 'Inh L1-4 VIP PENK'),
            "n43": ('n44', 'n46'),
            "n44": ('n45', 'Inh L1-2 SST BAGE2'),
            "n45": ('Inh L1 SST CHRNA4', 'Inh L1−2 GAD1 MC4R'),
            "n46": ('Inh L1-3 PAX6 SYT6', 'n47'),
            "n47": ('Inh L1-2 VIP TSPAN12', 'Inh L1-4 VIP CHRNA6'),
            "n48": ('n49', 'n50'),
            "n49": ('Inh L1-2 PAX6 CDH12', 'Inh L1-2 PAX6 TNFAIP8L3'),
            "n50": ('Inh L1 SST NMBR', 'n51'),
            "n51": ('n52', 'Inh L2-6 LAMP5 CA1'),
            "n52": ('Inh L1-4 LAMP5 LCP2', 'Inh L1-2 LAMP5 DBP'),
            "n53": ('n54', 'Inh L2-5 PVALB SCUBE3'),
            "n54": ('Inh L3-6 SST NPY', 'n55'),
            "n55": ('n61', 'n56'),
            "n56": ('Inh L5-6 GAD1 GLP1R', 'n57'),
            "n57": ('Inh L5-6 PVALB LGR5', 'n58'),
            "n58": ('n59', 'Inh L5-6 SST MIR548F2'),
            "n59": ('Inh L4-5 PVALB MEPE', 'n60'),
            "n60": ('Inh L2-4 PVALB WFDC2', 'Inh L4-6 PVALB SULF1'),
            "n61": ('n62', 'Inh L5-6 SST TH'),
            "n62": ('n65', 'n63'),
            "n63": ('n64', 'Inh L2-4 SST FRZB'),
            "n64": ('Inh L1-3 SST CALB1', 'Inh L3-5 SST ADGRG6'),
            "n65": ('Inh L3-6 SST HPGD', 'n66'),
            "n66": ('n67', 'Inh L4-5 SST STK32A'),
            "n67": ('n69', 'n68'),
            "n68": ('Inh L5-6 SST NPM1P10', 'Inh L4-6 SST GXYLT2'),
            "n69": ('Inh L4-6 SST B3GAT2', 'Inh L5-6 SST KLHDC8A'),
            "n70": ('n71', 'Micro L1-3 TYROBP'),
            "n71": ('n72', 'Endo L2-6 NOSTRIN'),
            "n72": ('n73', 'Oligo L1-6 OPALIN'),
            "n73": ('OPC L1-6 PDGFRA', 'n74'),
            "n74": ('Astro L1-6 FGFR3 SLC14A1', 'Astro L1-2 FGFR3 GFAP')
        }
        self.__init__(tree_arr)
        self.__isFinished = True
        thread_build.join()
        time.sleep(0.2)

        self.__waitingMessage = "Reading data in..."
        self.__isFinished = False
        thread_read = threading.Thread(target=self.__showProcess)
        thread_read.start()
        try:
            data = ad.read_h5ad(data_directory + "INPUT_DATA.h5ad")
        except KeyboardInterrupt:
            self.__isFinished = "Error"
            thread_read.join()
            raise
        except:
            self.__isFinished = "Error"
            thread_read.join()
            print("\033[1;31;40mError:\033[0m An error occurred during reading the dataset. The file may be broken. Do you want to redownload it? [y/n] ", end='')
            redownload = input()
            while redownload != 'y' and redownload != 'n':
                print("\033[1;31;40mError:\033[0m An error occurred during reading the dataset. The file may be broken. Do you want to redownload it? [y/n] ", end='')
                redownload = input()
            if redownload == 'y':
                self.clearDownload()
                return self.loadDefault()
            raise
        self.__isFinished = True
        thread_read.join()
        time.sleep(0.2)
        return data

    # Clear downloaded files from loadDefault().
    def clearDownload(self):
        clearDownload()

    # Read cells from a given directory.
    # data_directory: PathLike, representing the directory of the file, can be a ['pkl', 'csv', 'loom', 'h5ad', 'xlsx'] file, e.g. "~/xhx/Python/neuron_full.pkl";
    #           if data_directory is None: use default data directory.
    # branch_name: str, representing the target branch, e.g. "n48";
    #           if branch_name is None: choose default branch; if default is still None, read the whole dataset.
    # cluster_set: a list or tuple of strings containing all target clusters to choose;
    # use_cluster_set: bool, indicating whether to activate choose from cluster_set;
    # file_type: can be one of ['pkl', 'csv', 'loom', 'h5ad', 'xlsx'];
    # output: can be 'DataFrame' or 'AnnData', which indicates return type.
    # Return: a DataFrame or AnnData object.
    def readData(self, data_directory=None, branch_name=None, cluster_set=[], use_cluster_set=False, file_type=None, output=None):
        if data_directory is None:
            data_directory = self.__dataDirectory
        if not use_cluster_set and branch_name is None:
            branch_name = self.__branch
        data = None
        data_directory = data_directory.strip()
        if file_type is None:
            file_type = data_directory
        if not isinstance(file_type, str):
            raise TypeError("in method 'sctreeshap.sctreeshap.readData()' (in file '" + __file__ + "'), parameter 'file_type' receives " + str(type(file_type)) + ", expected <class 'str'>.")
        if file_type.endswith('csv'):
            data = pd.read_csv(data_directory)
        elif file_type.endswith('pkl'):
            data = pd.read_pickle(data_directory)
        elif file_type.endswith('loom'):
            data = ad.read_loom(data_directory)
        elif file_type.endswith('h5ad'):
            data = ad.read_h5ad(data_directory)
        elif file_type.endswith('xlsx'):
            data = ad.read_excel(data_directory)
        else:
            raise ValueError("in method 'sctreeshap.sctreeshap.readData()' (in file '" + __file__ + "'), parameter 'file_type' receives an unrecognized value: '" + file_type + "', expected 'csv', 'pkl', 'loom', 'h5ad' or 'xlsx'.")
        data = self.selectBranch(data, branch_name, cluster_set, use_cluster_set)
        if output is None:
            return data
        if not isinstance(output, str):
            raise TypeError("in method 'sctreeshap.sctreeshap.readData()' (in file '" + __file__ + "'), parameter 'output' receives " + str(type(output)) + ", expected <class 'str'>.")
        if output == "AnnData":
            if isinstance(data, pd.core.frame.DataFrame):
                return self.DataFrame_to_AnnData(data)
            else:
                return data
        elif output == "DataFrame":
            if isinstance(data, ad._core.anndata.AnnData):
                return self.AnnData_to_DataFrame(data)
            else:
                return data
        else:
            raise ValueError("in method 'sctreeshap.sctreeshap.readData()' (in file '" + __file__ + "'), parameter 'output' receives an unrecognized value: '" + str(output) + "', expected 'AnnData' or 'DataFrame'.")
    
    # Select cells whose cluster is under the given branch or in given cluster set.
    # data: AnnData or DataFrame;
    # branch_name: str, representing the target branch, e.g. "n48";
    #           if branch_name is None: choose default branch; if default is still None, read the whole dataset.
    # cluster_set: a list or tuple of strings containing all target clusters to choose;
    # use_cluster_set: bool, indicating whether to activate choose from cluster_set.
    # Return: a DataFrame or AnnData object.
    def selectBranch(self, data=None, branch_name=None, cluster_set=[], use_cluster_set=False):
        isAnnData = False
        if data is None:
            data = self.__dataSet
        if branch_name is None:
            branch_name = self.__branch
        if not isinstance(data, pd.core.frame.DataFrame) and not isinstance(data, ad._core.anndata.AnnData):
            raise TypeError("in method 'sctreeshap.sctreeshap.selectBranch()' (in file '" + __file__ + "'), paramter 'data' receives " + str(type(data)) + ", expected <class 'pandas.core.frame.DataFrame'> or <class 'anndata._core.anndata.AnnData'>.")
        if isinstance(data, ad._core.anndata.AnnData):
            isAnnData = True
            data = self.AnnData_to_DataFrame(data)
        cluster = data.columns.values[-1]
        if use_cluster_set:
            if (not isinstance(cluster_set, list) and not isinstance(cluster_set, tuple)) or len(cluster_set) == 0:
                cluster_set = self.__clusterSet
            data = data[data[cluster].isin(cluster_set)]
        elif branch_name != None:
            clusters = self.listBranch(branch_name)
            data = data[data[cluster].isin(clusters)]
        if isAnnData:
            return self.DataFrame_to_AnnData(data)
        else:
            return data
    
    # Merge all clusters under a given branch.
    # data: AnnData or DataFrame;
    # branch_name: str, the clusters under the branch will merge, relabelled as the branch_name;
    # Return: AnnData or DataFrame.
    def mergeBranch(self, data=None, branch_name=None):
        isAnnData = False
        if data is None:
            data = self.__dataSet
        if branch_name is None:
            branch_name = self.__branch
        if not isinstance(data, pd.core.frame.DataFrame) and not isinstance(data, ad._core.anndata.AnnData):
            raise TypeError("in method 'sctreeshap.sctreeshap.mergeBranch()' (in file '" + __file__ + "'), parameter 'data' receives " + str(type(data)) + ", expected <class 'pandas.core.frame.DataFrame'> or <class 'anndata._core.anndata.AnnData'>.")
        if isinstance(data, ad._core.anndata.AnnData):
            isAnnData = True
            data = self.AnnData_to_DataFrame(data)
        if branch_name != None:
            clusters = self.listBranch(branch_name)
            cluster = data.columns.values[-1]
            data.loc[data[data[cluster].isin(clusters)].index.tolist(), cluster] = branch_name
        if isAnnData:
            return self.DataFrame_to_AnnData(data)
        else:
            return data
        
    # Convert AnnData to DataFrame.
    # adata: an AnnData object.
    # Return: a DataFrame object.
    def AnnData_to_DataFrame(self, adata=None):
        if adata is None:
            adata = self.__dataSet
        if not isinstance(adata, ad._core.anndata.AnnData):
            raise TypeError("in method 'sctreeshap.sctreeshap.AnnData_to_DataFrame()' (in file '" + __file__ + "'), parameter 'adata' receives " + str(type(adata)) + ", expected <class 'anndata._core.anndata.AnnData'>.")
        return pd.concat([pd.DataFrame(adata.X, columns=adata.var.index.values).reset_index(drop=True), adata.obs.reset_index(drop=True)], axis=1, join="inner")

    # Convert DataFrame to AnnData.
    # data: a DataFrame object.
    # Return: an AnnData object.
    def DataFrame_to_AnnData(self, data=None):
        if data is None:
            data = self.__dataSet
        if not isinstance(data, pd.core.frame.DataFrame):
            raise TypeError("in method 'sctreeshap.sctreeshap.DataFrame_to_AnnData()' (in file '" + __file__ + "'), parameter 'data' receives " + str(type(data)) + ", expected <class 'pandas.core.frame.DataFrame'>.")
        cluster = data.columns.values[-1]
        obs = pd.DataFrame(data[cluster], columns=[cluster])
        obs[cluster] = obs[cluster].astype("category")
        data.drop([cluster], axis=1, inplace=True)
        var = pd.DataFrame(index=data.columns.values)
        X = np.array(data)
        return ad.AnnData(np.array(data), obs=obs, var=var, dtype="float")
    
    # Load human or mouse housekeeping gene set.
    # category: 'human' or 'mouse'.
    # Return: a list object.
    def loadHousekeeping(self, category):
        if not isinstance(category, str):
            raise TypeError("in method 'sctreeshap.sctreeshap.loadHousekeeping()' (in file '" + __file__ + "'), parameter 'category' receives " + str(type(category)) + ", expected <class 'str'>.")
        data_directory = __file__[:-13] + "sctreeshap_data"
        hkg = []
        if category == 'human':
            import os
            files = "Housekeeping_GenesHuman.csv"
            if not os.path.exists(data_directory) or not os.path.isfile(os.path.join(data_directory, files)):
                from pathlib import Path
                print("First time loading. Downloading " + files + "...")
                if not os.path.exists(data_directory):
                    os.mkdir(data_directory)
                path = Path(os.path.join(data_directory, files))
                url = "https://raw.githubusercontent.com/ForwardStar/sctreeshap/main/Housekeeping_GenesHuman.csv"
                download(url, path)
            file = open(os.path.join(data_directory, files), "r", encoding='utf-8')
            for lines in file.readlines()[1:]:
                lines = lines.split(';')
                hkg.append(lines[1])
        elif category == 'mouse':
            import os
            files = "Housekeeping_GenesMouse.csv"
            if not os.path.exists(data_directory) or not os.path.isfile(os.path.join(data_directory, files)):
                from pathlib import Path
                print("First time loading. Downloading " + files + "...")
                if not os.path.exists(data_directory):
                    os.mkdir(data_directory)
                path = Path(os.path.join(data_directory, files))
                url = "https://raw.githubusercontent.com/ForwardStar/sctreeshap/main/Housekeeping_GenesMouse.csv"
                download(url, path)
            file = open(os.path.join(data_directory, files), "r", encoding='utf-8')
            for lines in file.readlines()[1:]:
                lines = lines.split(';')
                hkg.append(lines[1])
        else:
            raise ValueError("in method 'sctreeshap.sctreeshap.loadHousekeeping()' (in file '" + __file__ + "'), parameter 'category' receives an unrecognized value: '" + category + "', expected 'human' or 'mouse'.")
        return hkg
            
    # Filter genes customly.
    # data: AnnData or DataFrame;
    # min_partial: float, to filter genes expressed in less than min_partial * 100% cells;
    #           if min_partial is None: do not filter.
    # gene_set: list or tuple, to filter genes appeared in gene_set;
    # gene_prefix: list or tuple, to filter genes with prefix in gene_prefix.
    # Return: a DataFrame or AnnData object.
    def geneFiltering(self, data=None, min_partial=None, gene_set=None, gene_prefix=None):
        isAnnData = False
        if data is None:
            data = self.__dataSet
        if not isinstance(data, pd.core.frame.DataFrame) and not isinstance(data, ad._core.anndata.AnnData):
            raise TypeError("in method 'sctreeshap.sctreeshap.geneFiltering()' (in file '" + __file__ + "'), parameter 'data' receives " + str(type(data)) + ", expected <class 'pandas.core.frame.DataFrame'> or <class 'anndata._core.anndata.AnnData'>.")
        if isinstance(data, ad._core.anndata.AnnData):
            isAnnData = True
            data = self.AnnData_to_DataFrame(data)
        if isinstance(gene_set, list) or isinstance(gene_set, tuple):
            target = [item for item in data.columns.values if item in gene_set]
            data = data.drop(target, axis=1)
        if isinstance(gene_prefix, list) or isinstance(gene_prefix, tuple):
            def check(item):
                for x in gene_prefix:
                    if item.startswith(x):
                        return True
                return False
            target = [item for item in data.columns.values if check(item)]
            data = data.drop(target, axis=1)
        if isinstance(min_partial, float):
            target = []
            cluster = data.columns.values[-1]
            for idx, _ in data.items():
                if idx != cluster:
                    expression = data[idx].to_numpy()
                    expression = expression[expression > 0]
                    if len(expression) / len(data) < min_partial:
                        target.append(idx)
            data = data.drop(target, axis=1)
        if isAnnData:
            return self.DataFrame_to_AnnData(data)
        else:
            return data

    # Do binary classification and generate shap figures.
    # data: an AnnData or DataFrame object;
    # cluster_name: str, the target cluster;
    # use_SMOTE: bool, indicates whether to use smote to oversample the data;
    # nthread: int, the number of running threads;
    # shap_params: dictionary, the shap plot parameters, indicating which kinds of figure to plot.
    def explainBinary(self, data=None, cluster_name=None, use_SMOTE=False, nthread=32, model='XGBClassifier', shap_params=None):        
        import shap
        from matplotlib import pyplot as plt
        from imblearn.over_sampling import SMOTE
        from sklearn.model_selection import train_test_split

        # Preprocessing data
        self.__waitingMessage = "Preprocessing data.."
        self.__isFinished = False
        thread_preprocessData = threading.Thread(target=self.__showProcess)
        thread_preprocessData.start()
        try:
            if data is None:
                data = self.__dataSet
            if not isinstance(data, pd.core.frame.DataFrame) and not isinstance(data, ad._core.anndata.AnnData):
                self.__isFinished = "Error"
                thread_preprocessData.join()
                time.sleep(0.2)
                raise TypeError("in method 'sctreeshap.sctreeshap.explainBinary()' (in file '" + __file__ + "'), parameter 'data' receives " + str(type(data)) + ", expected <class 'pandas.core.frame.DataFrame'> or <class 'anndata._core.anndata.AnnData'>.")
            if isinstance(data, ad._core.anndata.AnnData):
                data = self.AnnData_to_DataFrame(data)
            cluster = data.columns.values[-1]
            y = np.array(data[cluster])
            x = data.drop(columns=[cluster])
            if use_SMOTE:
                oversample = SMOTE()
                x, y = oversample.fit_resample(x, y)
            if cluster_name is None:
                cluster_name = self.__cluster
            y[y != cluster_name] = False
            y[y == cluster_name] = True
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 1234)
            x_train = x_train.reset_index(drop=True)
            x_test = x_test.reset_index(drop=True)
            self.__isFinished = True
            thread_preprocessData.join()
            time.sleep(0.2)
        except:
            self.__isFinished = "Error"
            thread_preprocessData.join()
            raise

        # Building the model
        self.__waitingMessage = "Building and training models.."
        self.__isFinished = False
        thread_buildModels = threading.Thread(target=self.__showProcess)
        thread_buildModels.start()
        try:
            if model == 'XGBClassifier':
                from xgboost import XGBClassifier
                self.__model = XGBClassifier(objective="binary:logistic", nthread=nthread, eval_metric="mlogloss", random_state=42, use_label_encoder=False)
            elif model == 'RandomForestClassifier':
                from sklearn.ensemble import RandomForestClassifier
                self.__model = RandomForestClassifier(n_jobs=nthread, random_state=42)
            elif model == 'DecisionTreeClassifier':
                print("\n\033[1;33;40mWarning:\033[0m DecisionTreeClassifier does not support multi-threading.")
                from sklearn.tree import DecisionTreeClassifier
                self.__model = DecisionTreeClassifier(random_state=42)
            else:
                self.__model = model
            self.__model.fit(x_train, y_train)
            self.__isFinished = True
            thread_buildModels.join()
        except:
            self.__isFinished = "Error"
            thread_buildModels.join()
            raise

        # Cross validation
        y_pred = self.__model.predict(x_test)
        accuracy = np.sum(y_pred == y_test) / len(y_pred) * 100
        print("Accuracy: %.4g%%" % accuracy)
        time.sleep(0.2)

        # Building the shap explainer
        self.__waitingMessage = "Building shap explainers.."
        self.__isFinished = False
        thread_buildShap = threading.Thread(target=self.__showProcess)
        thread_buildShap.start()
        try:
            if shap_params is None:
                shap_params = self.__shapParamsBinary
            if "model_output" not in shap_params or (shap_params["model_output"] != 'raw' and shap_params["model_output"] != 'probability'):
                shap_params["model_output"] = 'raw'
            if shap_params["model_output"] == 'raw':
                self.__explainer = shap.TreeExplainer(self.__model)
            elif shap_params["model_output"] == 'probability':
                print("\n\033[1;33;40mWarning:\033[0m There may be a segmentation fault if the number of features is too large.")
                self.__explainer = shap.TreeExplainer(self.__model, x_train, model_output='probability')
            else:
                self.__isFinished = "Error"
                thread_buildShap.join()
                raise ValueError(shap_params["model_output"])
            self.__shapValues = self.__explainer.shap_values(x_test)
            self.__isFinished = True
            thread_buildShap.join()
            time.sleep(0.2)
        except:
            self.__isFinished = "Error"
            thread_buildShap.join()
            raise

        # Generating shap figures
        print("Generating shap figures..")
        if "max_display" not in shap_params or not isinstance(shap_params["max_display"], int):
            shap_params["max_display"] = 10
        self.__maxDisplay = shap_params["max_display"]
        self.__featureNames = x.columns.values
        if "bar_plot" in shap_params and shap_params["bar_plot"]:
            print("     Drawing bar plot..")
            plt.figure(1)
            plt.title("Target Cluster: " + cluster_name)
            shap.summary_plot(self.__shapValues, x_test, feature_names=self.__featureNames, max_display=self.__maxDisplay, plot_type='bar', show=False)
            plt.show()
        if "beeswarm" in shap_params and shap_params["beeswarm"]:
            print("     Drawing beeswarm plot..")
            plt.figure(2)
            plt.title("Target Cluster: " + cluster_name)
            shap.summary_plot(self.__shapValues, x_test, feature_names=self.__featureNames, max_display=self.__maxDisplay)
            plt.show()
        if "force_plot" in shap_params and shap_params["force_plot"]:
            print("     Drawing force plot..")
            print("     \033[1;33;40mWarning:\033[0m: Force plot has not been stably supported yet.")
            shap.initjs()
            shap.plots.force(self.__explainer.expected_value, self.__shapValues, x_test, feature_names=self.__featureNames, show=False)
        if "heat_map" in shap_params and shap_params["heat_map"]:
            print("     Drawing heat map..")
            plt.figure(3)
            plt.title("Target Cluster: " + cluster_name)
            shap.plots.heatmap(self.__explainer(x_test), show=False)
            plt.show()
        if "decision_plot" in shap_params and shap_params["decision_plot"]:
            print("     Drawing decision plot..")
            plt.figure(4)
            plt.title("Target Cluster: " + cluster_name)
            y_pred = pd.DataFrame(y_pred).to_numpy()
            x_target = x_test[y_pred == 1]
            shap.decision_plot(self.__explainer.expected_value, self.__explainer.shap_values(x_target), x_target, link='logit', show=False)
            plt.show()

    # Do multi-classification and generate shap figures.
    # data: an AnnData or DataFrame object;
    # use_SMOTE: bool, indicates whether to use smote to oversample the data;
    # nthread: int, the number of running threads;
    # shap_params: dictionary, the shap plot parameters, indicating which kinds of figure to plot.
    def explainMulti(self, data=None, use_SMOTE=False, nthread=32, model='XGBClassifier', shap_params=None):
        import shap
        from xgboost import XGBClassifier
        from matplotlib import pyplot as plt
        from imblearn.over_sampling import SMOTE
        from sklearn.model_selection import train_test_split
        
        if shap_params is None:
            shap_params = self.__shapParamsMulti
        if "model_output" not in shap_params or (shap_params["model_output"] != 'raw' and shap_params["model_output"] != 'probability'):
            shap_params["model_output"] = 'raw'
        
        if shap_params["model_output"] == 'raw':
            # Preprocessing data
            self.__waitingMessage = "Preprocessing data.."
            self.__isFinished = False
            thread_preprocessData = threading.Thread(target=self.__showProcess)
            thread_preprocessData.start()
            try:
                if data is None:
                    data = self.__dataSet
                if not isinstance(data, pd.core.frame.DataFrame) and not isinstance(data, ad._core.anndata.AnnData):
                    self.__isFinished = "Error"
                    thread_preprocessData.join()
                    time.sleep(0.2)
                    raise TypeError("in method 'sctreeshap.explainMulti()' (in file '" + __file__ + "'), parameter 'data' receives " + str(type(data)) + ", expected <class 'pandas.core.frame.DataFrame'> or <class 'anndata._core.anndata.AnnData'>.")
                if isinstance(data, ad._core.anndata.AnnData):
                    data = self.AnnData_to_DataFrame(data)
                cluster = data.columns.values[-1]
                y = np.array(data[cluster])
                x = data.drop(columns=[cluster])
                if use_SMOTE:
                    oversample = SMOTE()
                    x, y = oversample.fit_resample(x, y)
                self.numOfClusters = 0
                self.clusterDict = {}
                [rows] = y.shape
                for i in range(rows):
                    if y[i] in self.clusterDict:
                        y[i] = self.clusterDict[y[i]]
                    else:
                        self.clusterDict[y[i]] = self.numOfClusters
                        y[i] = self.numOfClusters
                        self.numOfClusters += 1
                x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 1234)
                x_train = x_train.reset_index(drop=True)
                x_test = x_test.reset_index(drop=True)
                self.__isFinished = True
                thread_preprocessData.join()
                time.sleep(0.2)
                for key in self.clusterDict.keys():
                    print("     " + key + ": Class", self.clusterDict[key])
            except:
                self.__isFinished = "Error"
                thread_preprocessData.join()
                raise

            # Building the model
            self.__waitingMessage = "Building and training models.."
            self.__isFinished = False
            thread_buildModels = threading.Thread(target=self.__showProcess)
            thread_buildModels.start()
            try:
                if model == 'XGBClassifier':
                    self.__model = XGBClassifier(objective="multi:softmax", num_class=self.numOfClusters, nthread=nthread, eval_metric="mlogloss", random_state=42, use_label_encoder=False)    
                elif model == 'RandomForestClassifier':
                    from sklearn.ensemble import RandomForestClassifier
                    y_train = y_train.astype(str)
                    y_test = y_test.astype(str)
                    self.__model = RandomForestClassifier(n_jobs=nthread, random_state=42)
                elif model == 'DecisionTreeClassifier':
                    print("\n\033[1;33;40mWarning:\033[0m DecisionTreeClassifier does not support multi-threading.")
                    from sklearn.tree import DecisionTreeClassifier
                    y_train = y_train.astype(str)
                    y_test = y_test.astype(str)
                    self.__model = DecisionTreeClassifier(random_state=42)
                else:
                    y_train = y_train.astype(str)
                    y_test = y_test.astype(str)
                    self.__model = model
                self.__model.fit(x_train, y_train)
                self.__isFinished = True
                thread_buildModels.join()
            except:
                self.__isFinished = "Error"
                thread_buildModels.join()
                raise

            # Cross validation
            y_pred = self.__model.predict(x_test)
            accuracy = np.sum(y_pred == y_test) / len(y_pred) * 100
            print("Accuracy: %.4g%%" % accuracy)
            time.sleep(0.2)

            # Building the shap explainer
            self.__waitingMessage = "Building shap explainers.."
            self.__isFinished = False
            thread_buildShap = threading.Thread(target=self.__showProcess)
            thread_buildShap.start()
            try:
                self.__explainer = shap.TreeExplainer(self.__model)
                self.__shapValues = self.__explainer.shap_values(x_test)
                self.__isFinished = True
                thread_buildShap.join()
                time.sleep(0.2)
            except:
                self.__isFinished = "Error"
                thread_buildShap.join()
                raise

            # Generating shap figures
            print("Generating shap figures..")
            if "max_display" not in shap_params or not isinstance(shap_params["max_display"], int):
                shap_params["max_display"] = 10
            self.__maxDisplay = shap_params["max_display"]
            self.__featureNames = x.columns.values
            if "bar_plot" in shap_params and shap_params["bar_plot"]:
                print("     Drawing bar plot..")
                plt.figure(1)
                shap.summary_plot(self.__shapValues, x_test, feature_names=self.__featureNames, max_display=self.__maxDisplay, show=False)
                plt.show()
            if "beeswarm" in shap_params and shap_params["beeswarm"]:
                print("     Drawing beeswarm plot..")
                print("     \033[1;33;40mWarning:\033[0m I am not sure whether there is a segementation fault (core dumped). If so, please contact the developer.")
                print("     \033[1;33;40mWarning:\033[0m There is a problem on text size of shap figures. See issue #995 at https://github.com/slundberg/shap/issues/995")
                figure = plt.figure(2)
                rows = self.numOfClusters // 2 + self.numOfClusters % 2
                cols = 2
                index = 1
                for key in self.clusterDict.keys():
                    print("         Drawing cluster " + key + "...")
                    figure_sub = figure.add_subplot(rows, cols, index)
                    figure_sub.set_title("Target Cluster: " + key, fontsize=36)
                    shap.summary_plot(self.__shapValues[self.clusterDict[key]], x_test, feature_names=self.__featureNames, max_display=self.__maxDisplay, show=False)
                    index += 1
                figure.subplots_adjust(right=5, top=rows*3.5, hspace=0.2, wspace=0.2)
                plt.show()
            if "decision_plot" in shap_params and shap_params["decision_plot"]:
                print("     Drawing decision plot..")
                print("     \033[1;33;40mWarning:\033[0m I am not sure whether there is a segementation fault (core dumped). If so, please contact the developer.")
                print("     \033[1;33;40mWarning:\033[0m There is a problem on text size of shap figures. See issue #995 at https://github.com/slundberg/shap/issues/995")
                y_pred = pd.DataFrame(self.__model.predict_proba(x_test))
                figure = plt.figure(3)
                rows = self.numOfClusters // 2 + self.numOfClusters % 2
                cols = 2
                index = 1
                for key in self.clusterDict.keys():
                    print("         Drawing cluster " + key + "...")
                    y_pred_i = y_pred[y_pred.columns[self.clusterDict[key]]].to_numpy()
                    x_target = x_test[y_pred_i >= 0.9]
                    if len(x_target) == 0:
                        print("         \033[1;33;40mWarning:\033[0m Empty dataset, skipped. Try setting 'use_SMOTE=True'.")
                        index -= 1
                        continue
                    figure_sub = figure.add_subplot(rows, cols, index)
                    figure_sub.set_title("Target Cluster: " + key, fontsize=36)
                    shap.decision_plot(self.__explainer.expected_value[self.clusterDict[key]], self.__explainer.shap_values(x_target)[self.clusterDict[key]], x_target, link='logit', show=False)
                    index += 1
                figure.subplots_adjust(right=5, top=rows*3.5, hspace=0.2, wspace=0.2)
                plt.show()
        elif shap_params["model_output"] == 'probability':
            # Preprocessing data
            self.__waitingMessage = "Preprocessing data.."
            self.__isFinished = False
            thread_preprocessData = threading.Thread(target=self.__showProcess)
            thread_preprocessData.start()
            try:
                if data is None:
                    data = self.__dataSet
                if not isinstance(data, pd.core.frame.DataFrame) and not isinstance(data, ad._core.anndata.AnnData):
                    self.__isFinished = "Error"
                    thread_preprocessData.join()
                    time.sleep(0.2)
                    raise TypeError("in method 'sctreeshap.explainMulti()' (in file '" + __file__ + "'), parameter 'data' receives " + str(type(data)) + ", expected <class 'pandas.core.frame.DataFrame'> or <class 'anndata._core.anndata.AnnData'>.")
                if isinstance(data, ad._core.anndata.AnnData):
                    data = self.AnnData_to_DataFrame(data)
                cluster = data.columns.values[-1]
                y = np.array(data[cluster])
                x = data.drop(columns=[cluster])
                if use_SMOTE:
                    oversample = SMOTE()
                    x, y = oversample.fit_resample(x, y)
                self.numOfClusters = 0
                self.clusterDict = {}
                [rows] = y.shape
                for i in range(rows):
                    if y[i] in self.clusterDict:
                        y[i] = self.clusterDict[y[i]]
                    else:
                        self.clusterDict[y[i]] = self.numOfClusters
                        y[i] = self.numOfClusters
                        self.numOfClusters += 1
                x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 1234)
                x_train = x_train.reset_index(drop=True)
                x_test = x_test.reset_index(drop=True)
                y_train = [np.array(y_train) for i in range(self.numOfClusters)]
                y_train[0][y_train[0] == 0] = -1
                y_train[0][y_train[0] > 0] = False
                y_train[0][y_train[0] < 0] = True
                for i in range(1, self.numOfClusters):
                    y_train[i][y_train[i] != i] = False
                    y_train[i][y_train[i] == i] = True
                self.__isFinished = True
                thread_preprocessData.join()
                time.sleep(0.2)
                for key in self.clusterDict.keys():
                    print("     " + key + ": Class", self.clusterDict[key])
            except:
                self.__isFinished = "Error"
                thread_preprocessData.join()
                raise

            # Building the model
            self.__waitingMessage = "Building and training models.."
            self.__isFinished = False
            thread_buildModels = threading.Thread(target=self.__showProcess)
            thread_buildModels.start()
            try:
                self.__model = [XGBClassifier(objective="binary:logistic", nthread=nthread, eval_metric="mlogloss", random_state=42, use_label_encoder=False).fit(x_train, y_train[i]) for i in range(self.numOfClusters)]
                self.__isFinished = True
                thread_buildModels.join()
            except:
                self.__isFinished = "Error"
                thread_buildModels.join()
                raise

            # Cross validation
            y_pred = [self.__model[i].predict_proba(x_test)[:,1] for i in range(self.numOfClusters)]
            y_pred_multi = np.argmax(y_pred, axis=0)
            accuracy = np.sum(y_pred_multi == y_test) / y_pred_multi.shape[0] * 100
            print("Accuracy: %.4g%%" % accuracy)
            time.sleep(0.2)

            # Building the shap explainer
            self.__waitingMessage = "Building shap explainers.."
            self.__isFinished = False
            thread_buildShap = threading.Thread(target=self.__showProcess)
            thread_buildShap.start()
            try:
                print("\n\033[1;33;40mWarning:\033[0m There may be a segmentation fault if the number of features is too large.")
                if model != 'XGBClassifier':
                    print("\n\033[1;33;40mWarning:\033[0m For multi-classification, model_output='probability' only supports for model='XGBClassifier'.")
                self.__explainer = [shap.TreeExplainer(self.__model[i], x_train, model_output='probability') for i in range(self.numOfClusters)]
                self.__shapValues = [self.__explainer[i].shap_values(x_test) for i in range(self.numOfClusters)]
                self.__isFinished = True
                thread_buildShap.join()
                time.sleep(0.2)
            except:
                self.__isFinished = "Error"
                thread_buildShap.join()
                raise

            # Generating shap figures
            print("Generating shap figures..")
            if "max_display" not in shap_params or not isinstance(shap_params["max_display"], int):
                shap_params["max_display"] = 10
            self.__maxDisplay = shap_params["max_display"]
            self.__featureNames = x.columns.values
            if "bar_plot" in shap_params and shap_params["bar_plot"]:
                print("     Drawing bar plot..")
                plt.figure(1)
                shap.summary_plot(self.__shapValues, x_test, feature_names=self.__featureNames, max_display=self.__maxDisplay, show=False)
                plt.show()
            if "beeswarm" in shap_params and shap_params["beeswarm"]:
                print("     Drawing beeswarm plot..")
                print("     \033[1;33;40mWarning:\033[0m I am not sure whether there is a segementation fault (core dumped). If so, please contact the developer.")
                print("     \033[1;33;40mWarning:\033[0m There is a problem on text size of shap figures. See issue #995 at https://github.com/slundberg/shap/issues/995")
                figure = plt.figure(2)
                rows = self.numOfClusters // 2 + self.numOfClusters % 2
                cols = 2
                index = 1
                for key in self.clusterDict.keys():
                    print("         Drawing cluster " + key + "...")
                    figure_sub = figure.add_subplot(rows, cols, index)
                    figure_sub.set_title("Target Cluster: " + key, fontsize=36)
                    shap.summary_plot(self.__shapValues[self.clusterDict[key]], x_test, feature_names=self.__featureNames, max_display=self.__maxDisplay, show=False)
                    index += 1
                figure.subplots_adjust(right=5, top=rows*3.5, hspace=0.2, wspace=0.2)
                plt.show()
            if "decision_plot" in shap_params and shap_params["decision_plot"]:
                print("     Drawing decision plot..")
                print("     \033[1;33;40mWarning:\033[0m I am not sure whether there is a segementation fault (core dumped). If so, please contact the developer.")
                print("     \033[1;33;40mWarning:\033[0m There is a problem on text size of shap figures. See issue #995 at https://github.com/slundberg/shap/issues/995")
                figure = plt.figure(3)
                rows = self.numOfClusters // 2 + self.numOfClusters % 2
                cols = 2
                index = 1
                for key in self.clusterDict.keys():
                    print("         Drawing cluster " + key + "...")
                    x_target = x_test[y_pred[self.clusterDict[key]] >= 0.9]
                    if len(x_target) == 0:
                        print("         \033[1;33;40mWarning:\033[0m Empty dataset, skipped. Try setting 'use_SMOTE=True'.")
                        index -= 1
                        continue
                    figure_sub = figure.add_subplot(rows, cols, index)
                    figure_sub.set_title("Target Cluster: " + key, fontsize=36)
                    shap.decision_plot(self.__explainer[self.clusterDict[key]].expected_value, self.__explainer[self.clusterDict[key]].shap_values(x_target), x_target, link='logit', show=False)
                    index += 1
                figure.subplots_adjust(right=5, top=rows*3.5, hspace=0.2, wspace=0.2)
                plt.show()
        else:
            raise ValueError(shap_params["model_output"])
    
    def help(self, cmd=None):
        num_of_spaces = 110
        emptyline = ''
        if cmd == 'documentations' or cmd == 'apilist':
            documentations = '                                              \033[1;37;40mDocumentations\033[0m                                  '
            nameAndVersion = '                                            ' + __name__ + ': v' + __version__
            initialization = '\033[1;37;40mInitializations:\033[0m'
            sctreeshap = 'sctreeshap(): construct a sctreeshap object.'
            settings = '\033[1;37;40mSettings:\033[0m'
            setDataDirectory = 'setDataDirectory(): set default data directory.'
            setDataSet = 'setDataSet(): set default dataset.'
            setBranch = 'setBranch(): set default branch.'
            setCluster = 'setCluster(): set default cluster.'
            setClusterSet = 'setClusterSet(): set default target cluster set.'
            setShapParamsBinary = 'setShapParamsBinary(): set default shap plots parameters of explainBinary().'
            setShapParamsMulti = 'setShapParamsMulti(): set default shap plots parameters of explainMulti().'
            findCluster = 'findCluster(): find which branch a given cluster is in.'
            listBranch = 'listBranch(): list the clusters of a given branch.'
            loadDefault = 'loadDefault(): load default dataset and build default cluster tree.'
            clearDownload = 'clearDownload(): clear downloaded files from loadDefault().'
            dataprocessing = '\033[1;37;40mData processing:\033[0m'
            readData = 'readData(): read cells from a given directory.'
            selectBranch = 'selectBranch(): select cells whose cluster is under the given branch or in given cluster set.'
            mergeBranch = 'mergeBranch(): merge all clusters under a given branch.'
            AnnData_to_DataFrame = 'AnnData_to_DataFrame(): convert AnnData to DataFrame.'
            DataFrame_to_AnnData = 'DataFrame_to_AnnData(): convert DataFrame to AnnData.'
            loadHouseKeeping = 'loadHousekeeping(): load human or mouse housekeeping gene set.'
            geneFiltering = 'geneFiltering(): filter genes customly.'
            analysis = '\033[1;37;40mAnalysis:\033[0m'
            explainBinary = 'explainBinary(): do binary classification and generate shap figures.'
            explainMulti = 'explainMulti(): do multi-classification and generate shap figures.'
            getClassifier = "getClassifier(): get XGBClassifier of the last job (available after 'explainBinary()' or 'explainMulti()')."
            getExplainer = "getExplainer(): get shap explainer of the last job (available after 'explainBinary()' or 'explainMulti()')."
            getShapValues = "getShapValues(): get shap values of the last job (available after 'explainBinary()' or 'explainMulti()')."
            getTopGenes = "getTopGenes(): get top genes of max absolute mean shap values."
            return ' __' + '_' * num_of_spaces + '__ \n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + documentations + ' ' * (num_of_spaces - len(documentations) + 14) + '  |\n' \
                + '|  ' + nameAndVersion + ' ' * (num_of_spaces - len(nameAndVersion)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + initialization + ' ' * (num_of_spaces - len(initialization) + 14) + '  |\n' \
                + '|  ' + sctreeshap + ' ' * (num_of_spaces - len(sctreeshap)) + '  |\n' \
                + '|  ' + findCluster + ' ' * (num_of_spaces - len(findCluster)) + '  |\n' \
                + '|  ' + listBranch + ' ' * (num_of_spaces - len(listBranch)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + settings + ' ' * (num_of_spaces - len(settings) + 14) + '  |\n' \
                + '|  ' + setDataDirectory + ' ' * (num_of_spaces - len(setDataDirectory)) + '  |\n' \
                + '|  ' + setDataSet + ' ' * (num_of_spaces - len(setDataSet)) + '  |\n' \
                + '|  ' + setBranch + ' ' * (num_of_spaces - len(setBranch)) + '  |\n' \
                + '|  ' + setCluster + ' ' * (num_of_spaces - len(setCluster)) + '  |\n' \
                + '|  ' + setClusterSet + ' ' * (num_of_spaces - len(setClusterSet)) + '  |\n' \
                + '|  ' + setShapParamsBinary + ' ' * (num_of_spaces - len(setShapParamsBinary)) + '  |\n' \
                + '|  ' + setShapParamsMulti + ' ' * (num_of_spaces - len(setShapParamsMulti)) + '  |\n' \
                + '|  ' + loadDefault + ' ' * (num_of_spaces - len(loadDefault)) + '  |\n' \
                + '|  ' + clearDownload + ' ' * (num_of_spaces - len(clearDownload)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + dataprocessing + ' ' * (num_of_spaces - len(dataprocessing) + 14) + '  |\n' \
                + '|  ' + readData + ' ' * (num_of_spaces - len(readData)) + '  |\n' \
                + '|  ' + selectBranch + ' ' * (num_of_spaces - len(selectBranch)) + '  |\n' \
                + '|  ' + mergeBranch + ' ' * (num_of_spaces - len(mergeBranch)) + '  |\n' \
                + '|  ' + AnnData_to_DataFrame + ' ' * (num_of_spaces - len(AnnData_to_DataFrame)) + '  |\n' \
                + '|  ' + DataFrame_to_AnnData + ' ' * (num_of_spaces - len(DataFrame_to_AnnData)) + '  |\n' \
                + '|  ' + loadHouseKeeping + ' ' * (num_of_spaces - len(loadHouseKeeping)) + '  |\n' \
                + '|  ' + geneFiltering + ' ' * (num_of_spaces - len(geneFiltering)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + analysis + ' ' * (num_of_spaces - len(analysis) + 14) + '  |\n' \
                + '|  ' + explainBinary + ' ' * (num_of_spaces - len(explainBinary)) + '  |\n' \
                + '|  ' + explainMulti + ' ' * (num_of_spaces - len(explainMulti)) + '  |\n' \
                + '|  ' + getShapValues + ' ' * (num_of_spaces - len(getShapValues)) + '  |\n' \
                + '|  ' + getTopGenes + ' ' * (num_of_spaces - len(getTopGenes)) + '  |\n' \
                + '|__' + '_' * num_of_spaces + '__|'
        if cmd == 'sctreeshap':
            function = '\033[1;37;40msctreeshap.sctreeshap\033[0m'
            api = 'class sctreeshap.sctreeshap(tree_arr=None)'
            description =               'Description:   Construct a sctreeshap object.'
            tree_arr =                  'Parameters:    tree_arr: dictionary'
            tree_arr_description1 =     '               |  tree_arr[str] represents the node of name str in the cluster tree, can be a list or a tuple'
            tree_arr_description2 =     '               |  of strings, representing the name of childs of the node (from left to right).'
            tree_arr_description3 =     "               |  e.g. tree_arr['n1'] = ('n2', 'n70') represents a node named 'n1', whose left child is 'n2' "
            tree_arr_description4 =     "               |  and right child is 'n70'."
            tree_arr_description5 =     '               |  Note that you do not need to create nodes for clusters, since they are leaf nodes and have'
            tree_arr_description6 =     '               |  no childs.'
            return ' __' + '_' * num_of_spaces + '__ \n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + function + ' ' * (num_of_spaces - len(function) + 14) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + api + ' ' * (num_of_spaces - len(api)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + description + ' ' * (num_of_spaces - len(description)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + tree_arr + ' ' * (num_of_spaces - len(tree_arr)) + '  |\n' \
                + '|  ' + tree_arr_description1 + ' ' * (num_of_spaces - len(tree_arr_description1)) + '  |\n' \
                + '|  ' + tree_arr_description2 + ' ' * (num_of_spaces - len(tree_arr_description2)) + '  |\n' \
                + '|  ' + tree_arr_description3 + ' ' * (num_of_spaces - len(tree_arr_description3)) + '  |\n' \
                + '|  ' + tree_arr_description4 + ' ' * (num_of_spaces - len(tree_arr_description4)) + '  |\n' \
                + '|  ' + tree_arr_description5 + ' ' * (num_of_spaces - len(tree_arr_description5)) + '  |\n' \
                + '|  ' + tree_arr_description6 + ' ' * (num_of_spaces - len(tree_arr_description6)) + '  |\n' \
                + '|__' + '_' * num_of_spaces + '__|'
        if cmd == 'setDataDirectory':
            function = '\033[1;37;40msctreeshap.sctreeshap.setDataDirectory\033[0m'
            api = 'sctreeshap.sctreeshap.setDataDirectory(data_directory=None)'
            description =                   'Description: set default data directory.'
            data_directory =                'Parameters:  data_directory: PathLike'
            data_directory_description1 =   '             |  The directory of default input file, can be a .pkl file or a .csv file.'
            return ' __' + '_' * num_of_spaces + '__ \n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + function + ' ' * (num_of_spaces - len(function) + 14) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + api + ' ' * (num_of_spaces - len(api)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + description + ' ' * (num_of_spaces - len(description)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + data_directory + ' ' * (num_of_spaces - len(data_directory)) + '  |\n' \
                + '|  ' + data_directory_description1 + ' ' * (num_of_spaces - len(data_directory_description1)) + '  |\n' \
                + '|__' + '_' * num_of_spaces + '__|'
        if cmd == 'setDataSet':
            function = '\033[1;37;40msctreeshap.sctreeshap.setDataSet\033[0m'
            api = 'sctreeshap.sctreeshap.setDataSet(data=None)'
            description =                   'Description: set default dataset.'
            data =                          'Parameters:  data: DataFrame or AnnData'
            data_description1 =             '             |  The default dataset.'
            return ' __' + '_' * num_of_spaces + '__ \n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + function + ' ' * (num_of_spaces - len(function) + 14) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + api + ' ' * (num_of_spaces - len(api)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + description + ' ' * (num_of_spaces - len(description)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + data + ' ' * (num_of_spaces - len(data)) + '  |\n' \
                + '|  ' + data_description1 + ' ' * (num_of_spaces - len(data_description1)) + '  |\n' \
                + '|__' + '_' * num_of_spaces + '__|'
        if cmd == 'setBranch':
            function = '\033[1;37;40msctreeshap.sctreeshap.setBranch\033[0m'
            api = 'sctreeshap.sctreeshap.setBranch(branch_name=None)'
            description =                   'Description: set default branch.'
            branch_name =                          'Parameters:  branch_name: str'
            branch_name_description1 =             '             |  The default branch.'
            return ' __' + '_' * num_of_spaces + '__ \n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + function + ' ' * (num_of_spaces - len(function) + 14) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + api + ' ' * (num_of_spaces - len(api)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + description + ' ' * (num_of_spaces - len(description)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + branch_name + ' ' * (num_of_spaces - len(branch_name)) + '  |\n' \
                + '|  ' + branch_name_description1 + ' ' * (num_of_spaces - len(branch_name_description1)) + '  |\n' \
                + '|__' + '_' * num_of_spaces + '__|'
        if cmd == 'setCluster':
            function = '\033[1;37;40msctreeshap.sctreeshap.setCluster\033[0m'
            api = 'sctreeshap.sctreeshap.setCluster(cluster_name=None)'
            description =                   'Description: set default cluster.'
            cluster_name =                          'Parameters:  cluster_name: str'
            cluster_name_description1 =             '             |  The default cluster for binary classification.'
            return ' __' + '_' * num_of_spaces + '__ \n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + function + ' ' * (num_of_spaces - len(function) + 14) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + api + ' ' * (num_of_spaces - len(api)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + description + ' ' * (num_of_spaces - len(description)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + cluster_name + ' ' * (num_of_spaces - len(cluster_name)) + '  |\n' \
                + '|  ' + cluster_name_description1 + ' ' * (num_of_spaces - len(cluster_name_description1)) + '  |\n' \
                + '|__' + '_' * num_of_spaces + '__|'
        if cmd == 'setClusterSet':
            function = '\033[1;37;40msctreeshap.sctreeshap.setClusterSet\033[0m'
            api = 'sctreeshap.sctreeshap.setClusterSet(cluster_set=None)'
            description =                   'Description: set default target cluster set.'
            cluster_set =                          'Parameters:  cluster_set: list or tuple'
            cluster_set_description1 =             '             |  A list or tuple of strings to select data whose cluster is within it.'
            return ' __' + '_' * num_of_spaces + '__ \n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + function + ' ' * (num_of_spaces - len(function) + 14) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + api + ' ' * (num_of_spaces - len(api)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + description + ' ' * (num_of_spaces - len(description)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + cluster_set + ' ' * (num_of_spaces - len(cluster_set)) + '  |\n' \
                + '|  ' + cluster_set_description1 + ' ' * (num_of_spaces - len(cluster_set_description1)) + '  |\n' \
                + '|__' + '_' * num_of_spaces + '__|'
        if cmd == 'setShapParamsBinary':
            function = '\033[1;37;40msctreeshap.sctreeshap.setShapParamsBinary\033[0m'
            api = 'sctreeshap.sctreeshap.setShapParamsBinary(shap_params=None)'
            description =                   'Description: set default shap plots parameters of explainBinary().'
            shap_params =                          'Parameters:  shap_params: dictionary'
            shap_params_description1 =             '             |  Keys: ["max_display", "model_output", "bar_plot", "beeswarm", "force_plot", "heat_map",' 
            shap_params_description2 =             '             |  "decision_plot"]'
            shap_params_description3 =             "             |  Default values: [10, 'raw', True, True, False, False, False]"
            shap_params_description4 =             '             |  Determine the maximum number of genes you want to depict, whether to take raw shapley values '
            shap_params_description5 =             '             |  or probabilities as output, and what kinds of figures to output.'
            return ' __' + '_' * num_of_spaces + '__ \n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + function + ' ' * (num_of_spaces - len(function) + 14) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + api + ' ' * (num_of_spaces - len(api)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + description + ' ' * (num_of_spaces - len(description)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + shap_params + ' ' * (num_of_spaces - len(shap_params)) + '  |\n' \
                + '|  ' + shap_params_description1 + ' ' * (num_of_spaces - len(shap_params_description1)) + '  |\n' \
                + '|  ' + shap_params_description2 + ' ' * (num_of_spaces - len(shap_params_description2)) + '  |\n' \
                + '|  ' + shap_params_description3 + ' ' * (num_of_spaces - len(shap_params_description3)) + '  |\n' \
                + '|  ' + shap_params_description4 + ' ' * (num_of_spaces - len(shap_params_description4)) + '  |\n' \
                + '|  ' + shap_params_description5 + ' ' * (num_of_spaces - len(shap_params_description5)) + '  |\n' \
                + '|__' + '_' * num_of_spaces + '__|'
        if cmd == 'setShapParamsMulti':
            function = '\033[1;37;40msctreeshap.sctreeshap.setShapParamsMulti\033[0m'
            api = 'sctreeshap.sctreeshap.setShapParamsMulti(shap_params=None)'
            description =                   'Description: set default shap plots parameters of explainMulti().'
            shap_params =                          'Parameters:  shap_params: dictionary'
            shap_params_description1 =             '             |  Keys: ["max_display", "model_output", "bar_plot", "beeswarm", "decision_plot"]'
            shap_params_description2 =             "             |  Default values: [10, 'raw', True, False, False]"
            shap_params_description3 =             '             |  Determine the maximum number of genes you want to depict, whether to take raw shapley values '
            shap_params_description4 =             '             |  or probabilities as output, and what kinds of figures to output.'
            return ' __' + '_' * num_of_spaces + '__ \n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + function + ' ' * (num_of_spaces - len(function) + 14) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + api + ' ' * (num_of_spaces - len(api)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + description + ' ' * (num_of_spaces - len(description)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + shap_params + ' ' * (num_of_spaces - len(shap_params)) + '  |\n' \
                + '|  ' + shap_params_description1 + ' ' * (num_of_spaces - len(shap_params_description1)) + '  |\n' \
                + '|  ' + shap_params_description2 + ' ' * (num_of_spaces - len(shap_params_description2)) + '  |\n' \
                + '|  ' + shap_params_description3 + ' ' * (num_of_spaces - len(shap_params_description3)) + '  |\n' \
                + '|  ' + shap_params_description4 + ' ' * (num_of_spaces - len(shap_params_description4)) + '  |\n' \
                + '|__' + '_' * num_of_spaces + '__|'
        if cmd == 'findCluster':
            function = '\033[1;37;40msctreeshap.sctreeshap.findCluster\033[0m'
            api = 'sctreeshap.sctreeshap.findCluster(cluster_name=None)'
            description =                   'Description: find which branch a given cluster is in.'
            cluster_name =                          'Parameters:  cluster_name: str'
            cluster_name_description1 =             '             |  The target cluster.'
            return_description =                    'Return:      str, the path from root to the cluster.'
            return ' __' + '_' * num_of_spaces + '__ \n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + function + ' ' * (num_of_spaces - len(function) + 14) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + api + ' ' * (num_of_spaces - len(api)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + description + ' ' * (num_of_spaces - len(description)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + cluster_name + ' ' * (num_of_spaces - len(cluster_name)) + '  |\n' \
                + '|  ' + cluster_name_description1 + ' ' * (num_of_spaces - len(cluster_name_description1)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + return_description + ' ' * (num_of_spaces - len(return_description)) + '  |\n' \
                + '|__' + '_' * num_of_spaces + '__|'
        if cmd == 'listBranch':
            function = '\033[1;37;40msctreeshap.sctreeshap.listBranch\033[0m'
            api = 'sctreeshap.sctreeshap.listBranch(branch_name=None)'
            description =                   'Description: list the clusters of a given branch'
            branch_name =                          'Parameters:  branch_name: str'
            branch_name_description1 =             '             |  The target branch.'
            return_description =                    'Return:      list, all clusters under the branch.'
            return ' __' + '_' * num_of_spaces + '__ \n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + function + ' ' * (num_of_spaces - len(function) + 14) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + api + ' ' * (num_of_spaces - len(api)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + description + ' ' * (num_of_spaces - len(description)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + branch_name + ' ' * (num_of_spaces - len(branch_name)) + '  |\n' \
                + '|  ' + branch_name_description1 + ' ' * (num_of_spaces - len(branch_name_description1)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + return_description + ' ' * (num_of_spaces - len(return_description)) + '  |\n' \
                + '|__' + '_' * num_of_spaces + '__|'
        if cmd == 'loadDefault':
            function = '\033[1;37;40msctreeshap.sctreeshap.loadDefault\033[0m'
            api = "sctreeshap.sctreeshap.loadDefault()"
            description =                   'Description: load default dataset and build default cluster tree.'
            return_description =                      'Return:      AnnData.'
            return ' __' + '_' * num_of_spaces + '__ \n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + function + ' ' * (num_of_spaces - len(function) + 14) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + api + ' ' * (num_of_spaces - len(api)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + description + ' ' * (num_of_spaces - len(description)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + return_description + ' ' * (num_of_spaces - len(return_description)) + '  |\n' \
                + '|__' + '_' * num_of_spaces + '__|'
        if cmd == 'clearDownload':
            function = '\033[1;37;40msctreeshap.sctreeshap.clearDownload\033[0m'
            api = "sctreeshap.sctreeshap.clearDownload()"
            description =                   'Description: clear downloaded files from loadDefault().'
            return ' __' + '_' * num_of_spaces + '__ \n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + function + ' ' * (num_of_spaces - len(function) + 14) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + api + ' ' * (num_of_spaces - len(api)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + description + ' ' * (num_of_spaces - len(description)) + '  |\n' \
                + '|__' + '_' * num_of_spaces + '__|'
        if cmd == 'readData':
            function = '\033[1;37;40msctreeshap.sctreeshap.readData\033[0m'
            api = "sctreeshap.sctreeshap.readData(data_directory=None, branch_name=None, cluster_set=[], use_cluster_set=False, "
            api1 = "file_type=None, output=None)"
            description =                   'Description: read cells from a given directory.'
            data_directory =                          'Parameters:  data_directory: PathLike'
            data_directory_description1 =             "             |  The directory of the input file, can be a ['pkl', 'csv', 'loom', 'h5ad', 'xlsx'] file."
            branch_name =                             '             branch_name: str'
            branch_name_description1 =                '             |  If not None, filter cells not under the branch.'
            cluster_set =                             '             cluster_set: list or tuple'
            cluster_set_description1 =                '             |  A list or tuple of strings representing the target clusters.'
            use_cluster_set =                         '             use_cluster_set: bool'
            use_cluster_set_description1 =            '             |  If True, filter cells not with clusters in cluster_set.'
            file_type =                               '             file_type: str'
            file_type_description1 =                  "             |  Can be one of ['pkl', 'csv', 'loom', 'h5ad', 'xlsx']."
            output =                                  "             output: 'DataFrame' or 'AnnData'"
            output_description1 =                     '             |  Determine the return type of the function.'
            return_description =                      'Return:      AnnData or DataFrame.'
            return ' __' + '_' * num_of_spaces + '__ \n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + function + ' ' * (num_of_spaces - len(function) + 14) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + api + ' ' * (num_of_spaces - len(api)) + '  |\n' \
                + '|  ' + api1 + ' ' * (num_of_spaces - len(api1)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + description + ' ' * (num_of_spaces - len(description)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + data_directory + ' ' * (num_of_spaces - len(data_directory)) + '  |\n' \
                + '|  ' + data_directory_description1 + ' ' * (num_of_spaces - len(data_directory_description1)) + '  |\n' \
                + '|  ' + branch_name + ' ' * (num_of_spaces - len(branch_name)) + '  |\n' \
                + '|  ' + branch_name_description1 + ' ' * (num_of_spaces - len(branch_name_description1)) + '  |\n' \
                + '|  ' + cluster_set + ' ' * (num_of_spaces - len(cluster_set)) + '  |\n' \
                + '|  ' + cluster_set_description1 + ' ' * (num_of_spaces - len(cluster_set_description1)) + '  |\n' \
                + '|  ' + use_cluster_set + ' ' * (num_of_spaces - len(use_cluster_set)) + '  |\n' \
                + '|  ' + use_cluster_set_description1 + ' ' * (num_of_spaces - len(use_cluster_set_description1)) + '  |\n' \
                + '|  ' + file_type + ' ' * (num_of_spaces - len(file_type)) + '  |\n' \
                + '|  ' + file_type_description1 + ' ' * (num_of_spaces - len(file_type_description1)) + '  |\n' \
                + '|  ' + output + ' ' * (num_of_spaces - len(output)) + '  |\n' \
                + '|  ' + output_description1 + ' ' * (num_of_spaces - len(output_description1)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + return_description + ' ' * (num_of_spaces - len(return_description)) + '  |\n' \
                + '|__' + '_' * num_of_spaces + '__|'
        if cmd == 'selectBranch':
            function = '\033[1;37;40msctreeshap.sctreeshap.selectBranch\033[0m'
            api = "sctreeshap.sctreeshap.selectBranch(data, branch_name=None, cluster_set=[], use_cluster_set=False)"
            description =                   'Description: select cells whose cluster is under the given branch or in given cluster set.'
            data =                          'Parameters:  data: AnnData or DataFrame'
            branch_name =                             '             branch_name: str'
            branch_name_description1 =                '             |  If not None, filter cells not under the branch.'
            cluster_set =                             '             cluster_set: list or tuple'
            cluster_set_description1 =                '             |  A list or tuple of strings representing the target clusters.'
            use_cluster_set =                         '             use_cluster_set: bool'
            use_cluster_set_description1 =            '             |  If True, filter cells not with clusters in cluster_set.'
            return_description =                      'Return:      AnnData or DataFrame.'
            return ' __' + '_' * num_of_spaces + '__ \n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + function + ' ' * (num_of_spaces - len(function) + 14) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + api + ' ' * (num_of_spaces - len(api)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + description + ' ' * (num_of_spaces - len(description)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + data + ' ' * (num_of_spaces - len(data)) + '  |\n' \
                + '|  ' + branch_name + ' ' * (num_of_spaces - len(branch_name)) + '  |\n' \
                + '|  ' + branch_name_description1 + ' ' * (num_of_spaces - len(branch_name_description1)) + '  |\n' \
                + '|  ' + cluster_set + ' ' * (num_of_spaces - len(cluster_set)) + '  |\n' \
                + '|  ' + cluster_set_description1 + ' ' * (num_of_spaces - len(cluster_set_description1)) + '  |\n' \
                + '|  ' + use_cluster_set + ' ' * (num_of_spaces - len(use_cluster_set)) + '  |\n' \
                + '|  ' + use_cluster_set_description1 + ' ' * (num_of_spaces - len(use_cluster_set_description1)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + return_description + ' ' * (num_of_spaces - len(return_description)) + '  |\n' \
                + '|__' + '_' * num_of_spaces + '__|'
        if cmd == 'mergeBranch':
            function = '\033[1;37;40msctreeshap.sctreeshap.mergeBranch\033[0m'
            api = 'sctreeshap.sctreeshap.mergeBranch(data=None, branch_name=None)'
            description =                    'Description: merge all clusters under a given branch.'
            data =                          'Parameters:  data: AnnData or DataFrame'
            branch_name =                   '             branch_name: str'
            branch_name_description1 =      '             |  The clusters under the branch will merge, relabelled as the branch_name.'
            return_description =            'Return:      DataFrame or AnnData.'
            return ' __' + '_' * num_of_spaces + '__ \n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + function + ' ' * (num_of_spaces - len(function) + 14) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + api + ' ' * (num_of_spaces - len(api)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + description + ' ' * (num_of_spaces - len(description)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + data + ' ' * (num_of_spaces - len(data)) + '  |\n' \
                + '|  ' + branch_name + ' ' * (num_of_spaces - len(branch_name)) + '  |\n' \
                + '|  ' + branch_name_description1 + ' ' * (num_of_spaces - len(branch_name_description1)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + return_description + ' ' * (num_of_spaces - len(return_description)) + '  |\n' \
                + '|__' + '_' * num_of_spaces + '__|'
        if cmd == 'AnnData_to_DataFrame':
            function = '\033[1;37;40msctreeshap.sctreeshap.AnnData_to_DataFrame\033[0m'
            api = 'sctreeshap.sctreeshap.AnnData_to_DataFrame(adata)'
            description =                   'Description: convert AnnData to DataFrame.'
            adata =                          'Parameters:  adata: AnnData'
            adata_description1 =             '             |  An AnnData object in anndata package.'
            return_description =             'Return:      DataFrame.'
            return ' __' + '_' * num_of_spaces + '__ \n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + function + ' ' * (num_of_spaces - len(function) + 14) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + api + ' ' * (num_of_spaces - len(api)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + description + ' ' * (num_of_spaces - len(description)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + adata + ' ' * (num_of_spaces - len(adata)) + '  |\n' \
                + '|  ' + adata_description1 + ' ' * (num_of_spaces - len(adata_description1)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + return_description + ' ' * (num_of_spaces - len(return_description)) + '  |\n' \
                + '|__' + '_' * num_of_spaces + '__|'
        if cmd == 'DataFrame_to_AnnData':
            function = '\033[1;37;40msctreeshap.sctreeshap.DataFrame_to_AnnData\033[0m'
            api = 'sctreeshap.sctreeshap.DataFrame_to_AnnData(data)'
            description =                    'Description: convert DataFrame to AnnData.'
            data =                          'Parameters:  data: DataFrame'
            data_description1 =             '             |  A DataFrame object in pandas package.'
            return_description =             'Return:      AnnData.'
            return ' __' + '_' * num_of_spaces + '__ \n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + function + ' ' * (num_of_spaces - len(function) + 14) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + api + ' ' * (num_of_spaces - len(api)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + description + ' ' * (num_of_spaces - len(description)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + data + ' ' * (num_of_spaces - len(data)) + '  |\n' \
                + '|  ' + data_description1 + ' ' * (num_of_spaces - len(data_description1)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + return_description + ' ' * (num_of_spaces - len(return_description)) + '  |\n' \
                + '|__' + '_' * num_of_spaces + '__|'
        if cmd == 'loadHousekeeping':
            function = '\033[1;37;40msctreeshap.sctreeshap.loadHousekeeping\033[0m'
            api = 'sctreeshap.sctreeshap.loadHousekeeping(category)'
            description =                   'Description: load human or mouse housekeeping gene set.'
            category =                      "Parameters:  category: 'human' or 'mouse'"
            category_description1 =         '             |  Determine which housekeeping gene set to return.'
            return_description =            'Return:      list.'
            return ' __' + '_' * num_of_spaces + '__ \n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + function + ' ' * (num_of_spaces - len(function) + 14) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + api + ' ' * (num_of_spaces - len(api)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + description + ' ' * (num_of_spaces - len(description)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + category + ' ' * (num_of_spaces - len(category)) + '  |\n' \
                + '|  ' + category_description1 + ' ' * (num_of_spaces - len(category_description1)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + return_description + ' ' * (num_of_spaces - len(return_description)) + '  |\n' \
                + '|__' + '_' * num_of_spaces + '__|'
        if cmd == 'geneFiltering':
            function = '\033[1;37;40msctreeshap.sctreeshap.geneFiltering\033[0m'
            api = 'sctreeshap.sctreeshap.geneFiltering(data=None, min_partial=None, gene_set=None, gene_prefix=None)'
            description =                    'Description: filter genes customly.'
            data =                          'Parameters:  data: DataFrame or AnnData'
            min_partial =                   '             min_partial: float'
            min_partial_description1 =      '             |  If not None, filter genes expressed in less than min_partial * 100% cells.'
            gene_set =                      '             gene_set: list or tuple'
            gene_set_description1 =         '             |  A list or a tuple of genes to be filtered.'
            gene_prefix =                   '             gene_prefix: list or tuple'
            gene_prefix_description1 =      '             |  Genes with prefix in gene_prefix will be filtered.'
            return_description =             'Return:      AnnData or DataFrame.'
            return ' __' + '_' * num_of_spaces + '__ \n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + function + ' ' * (num_of_spaces - len(function) + 14) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + api + ' ' * (num_of_spaces - len(api)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + description + ' ' * (num_of_spaces - len(description)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + data + ' ' * (num_of_spaces - len(data)) + '  |\n' \
                + '|  ' + min_partial + ' ' * (num_of_spaces - len(min_partial)) + '  |\n' \
                + '|  ' + min_partial_description1 + ' ' * (num_of_spaces - len(min_partial_description1)) + '  |\n' \
                + '|  ' + gene_set + ' ' * (num_of_spaces - len(gene_set)) + '  |\n' \
                + '|  ' + gene_set_description1 + ' ' * (num_of_spaces - len(gene_set_description1)) + '  |\n' \
                + '|  ' + gene_prefix + ' ' * (num_of_spaces - len(gene_prefix)) + '  |\n' \
                + '|  ' + gene_prefix_description1 + ' ' * (num_of_spaces - len(gene_prefix_description1)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + return_description + ' ' * (num_of_spaces - len(return_description)) + '  |\n' \
                + '|__' + '_' * num_of_spaces + '__|'
        if cmd == 'explainBinary':
            function = '\033[1;37;40msctreeshap.sctreeshap.explainBinary\033[0m'
            api =                           'sctreeshap.sctreeshap.explainBinary(data=None, cluster_name=None, use_SMOTE=False, nthread=32, '
            api1 =                          "model='XGBClassifier', shap_params=None)"
            description =                   'Description: do binary classification and generate shap figures.'
            data =                          'Parameters:  data: DataFrame or AnnData'
            cluster_name =                  '             cluster_name: str'
            cluster_name_description1 =     '             |  The target cluster for classification.'
            use_SMOTE =                     '             use_SMOTE: bool'
            use_SMOTE_description1 =        '             |  True if you want to use SMOTE to resample.'
            nthread =                       '             nthread: int'
            nthread_description1 =          '             |  The number of running threads.'
            model =                         '             model: str, or a sklearn model'
            model_description1 =            "             |  A model type in ['XGBClassifier', 'RandomForestClassifier', 'DecisionTreeClassifier'], or a"
            model_description2 =            '             |  sklearn model you have defined.'
            shap_params =                   '             shap_params: dictionary'
            shap_params_description1 =      '             |  Keys: ["max_display", "model_output", "bar_plot", "beeswarm", "force_plot", "heat_map", '
            shap_params_description2 =      '             |  "decision_plot"]'
            shap_params_description3 =      '             |  Values: "max_display" reflects an int, which determines the maximum number of genes to display'
            shap_params_description4 =      '             |  in shap figures, "model_output" can be "raw" or "probability", while each other key is '
            shap_params_description5 =      '             |  reflected to a bool which indicates whether to output this kind of shap figures.'
            return ' __' + '_' * num_of_spaces + '__ \n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + function + ' ' * (num_of_spaces - len(function) + 14) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + api + ' ' * (num_of_spaces - len(api)) + '  |\n' \
                + '|  ' + api1 + ' ' * (num_of_spaces - len(api1)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + description + ' ' * (num_of_spaces - len(description)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + data + ' ' * (num_of_spaces - len(data)) + '  |\n' \
                + '|  ' + cluster_name + ' ' * (num_of_spaces - len(cluster_name)) + '  |\n' \
                + '|  ' + cluster_name_description1 + ' ' * (num_of_spaces - len(cluster_name_description1)) + '  |\n' \
                + '|  ' + use_SMOTE + ' ' * (num_of_spaces - len(use_SMOTE)) + '  |\n' \
                + '|  ' + use_SMOTE_description1 + ' ' * (num_of_spaces - len(use_SMOTE_description1)) + '  |\n' \
                + '|  ' + nthread + ' ' * (num_of_spaces - len(nthread)) + '  |\n' \
                + '|  ' + nthread_description1 + ' ' * (num_of_spaces - len(nthread_description1)) + '  |\n' \
                + '|  ' + model + ' ' * (num_of_spaces - len(model)) + '  |\n' \
                + '|  ' + model_description1 + ' ' * (num_of_spaces - len(model_description1)) + '  |\n' \
                + '|  ' + model_description2 + ' ' * (num_of_spaces - len(model_description2)) + '  |\n' \
                + '|  ' + shap_params + ' ' * (num_of_spaces - len(shap_params)) + '  |\n' \
                + '|  ' + shap_params_description1 + ' ' * (num_of_spaces - len(shap_params_description1)) + '  |\n' \
                + '|  ' + shap_params_description2 + ' ' * (num_of_spaces - len(shap_params_description2)) + '  |\n' \
                + '|  ' + shap_params_description3 + ' ' * (num_of_spaces - len(shap_params_description3)) + '  |\n' \
                + '|  ' + shap_params_description4 + ' ' * (num_of_spaces - len(shap_params_description4)) + '  |\n' \
                + '|  ' + shap_params_description5 + ' ' * (num_of_spaces - len(shap_params_description5)) + '  |\n' \
                + '|__' + '_' * num_of_spaces + '__|'
        if cmd == 'explainMulti':
            function = '\033[1;37;40msctreeshap.sctreeshap.explainMulti\033[0m'
            api =                           "sctreeshap.sctreeshap.explainMulti(data=None, use_SMOTE=False, nthread=32, model='XGBClassifier', "
            api1 =                          "shap_params=None)"
            description =                   'Description: do multi-classification and generate shap figures.'
            data =                          'Parameters:  data: DataFrame or AnnData'
            use_SMOTE =                     '             use_SMOTE: bool'
            use_SMOTE_description1 =        '             |  True if you want to use SMOTE to resample.'
            nthread =                       '             nthread: int'
            nthread_description1 =          '             |  The number of running threads.'
            model =                         '             model: str, or a sklearn model'
            model_description1 =            "             |  A model type in ['XGBClassifier', 'RandomForestClassifier', 'DecisionTreeClassifier'], or a"
            model_description2 =            '             |  sklearn model you have defined.'
            shap_params =                   '             shap_params: dictionary'
            shap_params_description1 =      '             |  Keys: ["max_display", "model_output", "bar_plot", "beeswarm", "decision_plot"]'
            shap_params_description2 =      '             |  Values: "max_display" reflects an int, which determines the maximum number of genes to display'
            shap_params_description3 =      '             |  in shap figures, "model_output" can be "raw" or "probability", while each other key is '
            shap_params_description4 =      '             |  reflected to a bool which indicates whether to output this kind of shap figures.'
            return ' __' + '_' * num_of_spaces + '__ \n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + function + ' ' * (num_of_spaces - len(function) + 14) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + api + ' ' * (num_of_spaces - len(api)) + '  |\n' \
                + '|  ' + api1 + ' ' * (num_of_spaces - len(api1)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + description + ' ' * (num_of_spaces - len(description)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + data + ' ' * (num_of_spaces - len(data)) + '  |\n' \
                + '|  ' + use_SMOTE + ' ' * (num_of_spaces - len(use_SMOTE)) + '  |\n' \
                + '|  ' + use_SMOTE_description1 + ' ' * (num_of_spaces - len(use_SMOTE_description1)) + '  |\n' \
                + '|  ' + nthread + ' ' * (num_of_spaces - len(nthread)) + '  |\n' \
                + '|  ' + nthread_description1 + ' ' * (num_of_spaces - len(nthread_description1)) + '  |\n' \
                + '|  ' + model + ' ' * (num_of_spaces - len(model)) + '  |\n' \
                + '|  ' + model_description1 + ' ' * (num_of_spaces - len(model_description1)) + '  |\n' \
                + '|  ' + model_description2 + ' ' * (num_of_spaces - len(model_description2)) + '  |\n' \
                + '|  ' + shap_params + ' ' * (num_of_spaces - len(shap_params)) + '  |\n' \
                + '|  ' + shap_params_description1 + ' ' * (num_of_spaces - len(shap_params_description1)) + '  |\n' \
                + '|  ' + shap_params_description2 + ' ' * (num_of_spaces - len(shap_params_description2)) + '  |\n' \
                + '|  ' + shap_params_description3 + ' ' * (num_of_spaces - len(shap_params_description3)) + '  |\n' \
                + '|  ' + shap_params_description4 + ' ' * (num_of_spaces - len(shap_params_description4)) + '  |\n' \
                + '|__' + '_' * num_of_spaces + '__|'
        if cmd == 'getShapValues':
            function = '\033[1;37;40msctreeshap.sctreeshap.getShapValues\033[0m'
            api = 'sctreeshap.sctreeshap.getShapValues()'
            description =                    "Description: get shap values of the last job (available after 'a.explainBinary()' or 'a.explainMulti()')."
            return_description =             'Return:      ndarray.'
            return ' __' + '_' * num_of_spaces + '__ \n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + function + ' ' * (num_of_spaces - len(function) + 14) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + api + ' ' * (num_of_spaces - len(api)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + description + ' ' * (num_of_spaces - len(description)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + return_description + ' ' * (num_of_spaces - len(return_description)) + '  |\n' \
                + '|__' + '_' * num_of_spaces + '__|'
        if cmd == 'getTopGenes':
            function = '\033[1;37;40msctreeshap.sctreeshap.getTopGenes\033[0m'
            api = 'sctreeshap.sctreeshap.getTopGenes(max_display=None, shap_values=None, feature_names=None)'
            description =                    'Description: get top genes of max absolute mean shap values. (You can just simply call it without any '
            description1 =                   '             parameters after explainBinary() or explainMulti()).'
            max_display =                    'Parameters:  max_display: int'
            max_display_description1 =       '             |  The the number of top genes you want to derive.'
            shap_values =                    '             shap_values: list or ndarray'
            shap_values_description1 =       '             |  This can be derived from getShapValues(), defaultly from last explainBinary()/explainMulti().'
            feature_names =                  '             feature_names: ndarray, list or tuple'
            feature_names_description1 =     '             |  The gene set (columns of cell-gene matrix), must correspond to order of shap_values, defaultly'
            feature_names_description2 =     '             |  from last explainBinary()/explainMulti().'
            return_description =             'Return:      ndarray, an ordered set of top genes of maximum absolute mean shap values.'
            return ' __' + '_' * num_of_spaces + '__ \n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + function + ' ' * (num_of_spaces - len(function) + 14) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + api + ' ' * (num_of_spaces - len(api)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + description + ' ' * (num_of_spaces - len(description)) + '  |\n' \
                + '|  ' + description1 + ' ' * (num_of_spaces - len(description1)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + max_display + ' ' * (num_of_spaces - len(max_display)) + '  |\n' \
                + '|  ' + max_display_description1 + ' ' * (num_of_spaces - len(max_display_description1)) + '  |\n' \
                + '|  ' + shap_values + ' ' * (num_of_spaces - len(shap_values)) + '  |\n' \
                + '|  ' + shap_values_description1 + ' ' * (num_of_spaces - len(shap_values_description1)) + '  |\n' \
                + '|  ' + feature_names + ' ' * (num_of_spaces - len(feature_names)) + '  |\n' \
                + '|  ' + feature_names_description1 + ' ' * (num_of_spaces - len(feature_names_description1)) + '  |\n' \
                + '|  ' + feature_names_description2 + ' ' * (num_of_spaces - len(feature_names_description2)) + '  |\n' \
                + '|  ' + emptyline + ' ' * (num_of_spaces - len(emptyline)) + '  |\n' \
                + '|  ' + return_description + ' ' * (num_of_spaces - len(return_description)) + '  |\n' \
                + '|__' + '_' * num_of_spaces + '__|'
        if cmd != None:
            return "Function '" + cmd + "' not found!"
        while True:
            print('* ', end='')
            cmd = input().strip()
            if cmd == 'EXIT':
                return None
            else:
                print(self.help(cmd))

checkUpdates()
