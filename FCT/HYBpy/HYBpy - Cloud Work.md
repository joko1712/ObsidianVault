
## **Step 1: Create a Compute Engine Virtual Machine (VM)**

1. Go to the **Google Cloud Console**.
    
2. Navigate to **Compute Engine** > **VM instances**.
    
3. **Create Instance**:
    - **Name**: `hybtrain-vm`
    - **Machine type**: Choose one with sufficient CPU and memory.
    - **Boot Disk**:
        - 1º OS: Debian Deep Learning. - Performance:
        - 2º OS: Debian Deep Learning with cuda activated. - Performance: 
    - **Firewall**: Enable **HTTP** and **HTTPS** traffic.
4. **Create**

## **Step 2: Connect to the VM and Set Up the Environment**

1. SSH into the VM from the Cloud Console or via `gcloud`:
	gcloud compute ssh hybtrain-vm

2.  **Update the system and install dependencies**:
	sudo apt update && sudo apt upgrade -y
	sudo apt install -y python3 python3-pip git
	

3. **Clone your code repository**:
	git clone https://github.com/joko1712/HYBpy
	cd your-repo

4. Install required Python packages:
	pip3 install -r requirements.txt

5. Verify `main.py` works locally:
	python3 main.py


