a
    �Ǧ`  �                   @   s   d dl Z G dd� d�ZdS )�    Nc                   @   s   e Zd Zdd� Zdd� ZdS )�Buttonc                 C   sV   |� � }|�� }tj�|t|| �t|| �f�| _| j�� | _||f| j_	d| _
d S )NF)�	get_width�
get_height�pygame�	transform�scale�int�image�get_rect�rect�topleft�clicked)�self�x�yr	   r   �width�height� r   �IC:\Users\Admin\Dropbox\Docs\Programming\pygame\tutorials\Button\button.py�__init__   s    $zButton.__init__c                 C   sv   d}t j�� }| j�|�r@t j�� d dkr@| jdkr@d| _d}t j�� d dkrXd| _|�| j| jj	| jj
f� |S )NFr   �   T)r   �mouse�get_posr   �collidepoint�get_pressedr   �blitr	   r   r   )r   �surface�action�posr   r   r   �draw   s    
zButton.drawN)�__name__�
__module__�__qualname__r   r   r   r   r   r   r      s   r   )r   r   r   r   r   r   �<module>   s   