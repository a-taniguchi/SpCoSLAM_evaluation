# Evaluation / Visualization for SpCoSLAM data  

These files are the codes for the evaluation or the visualization in SpCoSLAM.  
These codes were used for experiments in our IROS paper.  

[Note] It includes cluttered codes and unused codes.  

-----
[How to visualize the position distributions on rviz]  
`roscore`  
`rviz -d ./*/SpCoSLAM/learning/saveSpCoMAP_online.rviz `  
`python ./autovisualization.py p30a20g10sfix008`  

In case of individual specification  
`rosrun map_server map_server ./p30a20g10sfix008/map/map361.yaml`  
`python ./new_place_draw.py p30a20g10sfix008 50 23 `  


-----
If you use this program to publish something, please describe the following citation information.  

Reference  
- Akira Taniguchi, Yoshinobu Hagiwara, Tadahiro Taniguchi, and Tetsunari Inamura, "Online Spatial Concept and Lexical Acquisition with Simultaneous Localization and Mapping", IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS2017), 2017.  
    - Original paper: https://arxiv.org/abs/1704.04664  

- Akira Taniguchi, Yoshinobu Hagiwara, Tadahiro Taniguchi, and Tetsunari Inamura, "An Improved and Scalable Online Learning of Spatial Concepts and Language Models with Mapping", arXiv:1803.03481, 2018. (Preprint submitted)  
    - Original paper: https://arxiv.org/abs/1803.03481  


Sample video: https://youtu.be/z73iqwKL-Qk


2018/05/18 Akira Taniguchi  
2019/01/08 Akira Taniguchi (update)  
