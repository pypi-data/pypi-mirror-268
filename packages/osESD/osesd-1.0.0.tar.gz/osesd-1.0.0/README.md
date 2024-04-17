
# Automated Online Sequential ESD (Python)

This package includes Python codes for online sequential ESD(osESD), a variation of GESD tests.  
It is a statistical testing method for anomaly detection in univariate time series datasets.  
We provide osESD and an automated grid search method auto-osESD.  
Auto-osESD can be used to find the best parameters for a specific dataset,  
using parameters either provided explicitly or basic parameters if not provided.  
Original paper can be found in [LINK].  

## Installation
### 1. Clone repository.
Clone or download zip. file of our repository into local device.

### 2. Download dependencies.
Download dependencies written in requirements.txt.  
This can be easily done by running the below code in command prompt.  
```
pip install -r requirements.txt
```


### 3. Datasets.
URL link to google drive with datasets used in testing and replication.

[Dataset Link](https://drive.google.com/drive/folders/1ng4eqciexoEOJp_T5D4nwXVN7OVQfBp7?usp=sharing)

Yahoo! benchmark datasets are not included in this drive due to Yahoo! license policies.
These can be found and downloaded in 
[Yahoo dataset](https://webscope.sandbox.yahoo.com/catalog.php?datatype=s&did=70&guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAAtaVR04P1M9zgds3PzfnAtAVhsUOz4pZiQ5UEtlYB3z1JjyVl2oO-GopA8MTYZoEUJ4AhNDXHLP5SoGcCqai8FnucvuOsaZLXiTF9Xo4-4mXTqcRoUVT-SrkziayaB0j0MDrrVmMyZD0LlaPgFoPJkyePrvECHAfNxfaH_6YjyC) .


## Versions
Python = 3.8.16    
argparse = 1.1  
numpy = 1.24.3  
pandas = 1.5.3  
torch = 1.13.1  
matplotlib = 3.7.0  
scikit-learn = 1.2.1  
scipy = 1.10.1  
rrcf = 0.4.4  






## Example Usage

After cloning this repository and installing all dependencies, one can run our osESD method with the below code,  
with data_name being directory to dataset and result_directory being directory to where indices of anomalies be exported.  

```
python main.py --dataset data_name --result_directory result_directory
```

To run auto-osESD, the below code should be run.  

```
python auto_osESD.py --dataset data_name --result_directory result_directory
```

To change parameters and provide new ones, the below code should be modified and run.  

```
python auto_oseSD.py --dataset data_name --result_directory result_directory
--labeled True --sizes "50,100,150,200" --conditions "0,1" --maxrs "3,5,7,10"
--dwins "2,5,10,30" --rwins "4,5,10,30" --alphas "0.0001,0.005,0.01,0.05"
--weights "0,0,1,0.1" --learning_length 0.15 --min_max_switch False
```

Finally, if the dataset is unlabeled, then one should set '--labeled' to False.  
```
python auto_osESD.py --dataset data_name --result_directory result_directory --labeled false
```

