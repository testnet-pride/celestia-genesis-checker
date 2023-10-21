#### Install required packages
```bash
sudo apt update && \
sudo apt install python3 wget git -y
```
#### Clone the repo
```
git clone https://github.com/testnet-pride/celestia-genesis-checker
```
#### Install python packages with pip
```bash
cd $HOME/celestia-genesis-checker && \
pip3 install -r requirements.txt
```
### Edit wallets.txt which is located in $HOME/celestia-genesis-checker/wallets.txt 
#### Make it look like this (one wallet = one line):
```
celestia10022mzmrheg2fl3s88fc2eg9vstt8s4s8983k6
celestia10022mzmrheg2fl3s88fc2eg9vstt8s4s8983k6
celestia10022mzmrheg2fl3s88fc2eg9vstt8s4s8983k6
celestia10022mzmrheg2fl3s88fc2eg9vstt8s4s8983k6
```
### Run the script
```python
python3 $HOME/celestia-genesis-checker/main.py
```
### Output will look like::
```bash
+-------------------------------------------------+-------------------+
| Address                                         |   Balance in $TIA |
+=================================================+===================+
| celestia10022mzmrheg2fl3s88fc2eg9vstt8s4s8983k6 |               163 |
+-------------------------------------------------+-------------------+
| celestia18am0mqlaqnkr7rv07wxdgn2hcax34v8e7uqqns |               163 |
+-------------------------------------------------+-------------------+
| celestia18at52hrq9ywg8fegwkfalka6fmcxv006zwf0g6 |               294 |
+-------------------------------------------------+-------------------+
| celestia18auckwd7wa69nzyy6jam57hepzhxqmy3tz4gkn |               257 |
+-------------------------------------------------+-------------------+
| celestia18awezajjkec6vqdlsug44jhu7gz7xa7622ppsw |               163 |
+-------------------------------------------------+-------------------+
| celestia18azycqh8wm4y8angu675k2hy0ap4sgy4qaxmd2 |               229 |
+-------------------------------------------------+-------------------+
| celestia1d2qrp6sfhmt4ds5s0vu2fy9fz4w2sydzcnn4x7 |               257 |
+-------------------------------------------------+-------------------+
| celestia1dwny2nmwhav4gkm5ey490gtuy88ut0zclf57a3 |               294 |
+-------------------------------------------------+-------------------+
| celestia1f0kauf66nm2t4f9k0zeq67pt382u4gnpv6fxhn |               163 |
+-------------------------------------------------+-------------------+
| celestia1f0nskag925ch9287mfxdpxnu9ke7sex33lafxc |               163 |
+-------------------------------------------------+-------------------+
| Total $TIA                                      |              2146 |
+-------------------------------------------------+-------------------+
```
