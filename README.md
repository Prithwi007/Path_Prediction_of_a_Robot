# Path_Prediction_of_a_Robot
The objective of this research is to predict the path of robot using a proposed algorithm. The environment consists of multiple observers placed at different locations, which can detect the position of the robots. However, the observers have limited range of vision, and they can only detect robots when they come within their predefined range.

The range of vision for each observer is circular, and the robots are detected when they enter this range. As a result, only a small portion of the robot's path can be observed using collision detection techniques. This path is generated periodically based on parameters such as depth, displacement, and fractal patterns.

# Bezier Curves for Path Prediction in Robot Navigation

The inherent properties of Bezier curves make them suitable for path prediction in the context of robot navigation. This README provides an overview of how Bezier curves can be utilized to represent complex trajectories with smoothness and continuity.

## Bezier Curve Formula

The Bezier curve formula is given by:

![Bezier Curve Formula](https://render.githubusercontent.com/render/math?math=P(t)%20%3D%20%5Csum_%7Bi%3D0%7D%5E%7Bn%7D%20B_i^n(t)%20%5Ccdot%20P_t) .... (i)

where:

![Binomial Coefficient](https://render.githubusercontent.com/render/math?math=B_i^n(t)%20%3D%20%5Cbinom%7Bn%7D%7Bi%7D%20%5Ccdot%20t%5Ei%20%5Ccdot%20(1-t)%5E%7Bn-i%7D) .... (ii)

![image](https://github.com/Prithwi007/Path_Prediction_of_a_Robot/assets/43519651/7def1460-1c37-4183-8f60-19e060c07878)

![image](https://github.com/Prithwi007/Path_Prediction_of_a_Robot/assets/43519651/17b6cc1d-8b87-4c1c-bf6c-35afb8578cd9)

![image](https://github.com/Prithwi007/Path_Prediction_of_a_Robot/assets/43519651/1b9ffad8-601c-4d2a-bf8b-655aef55b518)

![image](https://github.com/Prithwi007/Path_Prediction_of_a_Robot/assets/43519651/e1fb38f8-6fb2-495b-b630-d3831f79a077)

![image](https://github.com/Prithwi007/Path_Prediction_of_a_Robot/assets/43519651/ab8b5e8d-9327-4ac1-be9d-dc52b721bcbb)


