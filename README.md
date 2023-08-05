# Path_Prediction_of_a_Robot
The objective of this research is to predict the path of robot using a proposed algorithm. The environment consists of multiple observers placed at different locations, which can detect the position of the robots. However, the observers have limited range of vision, and they can only detect robots when they come within their predefined range.

The range of vision for each observer is circular, and the robots are detected when they enter this range. As a result, only a small portion of the robot's path can be observed using collision detection techniques. This path is generated periodically based on parameters such as depth, displacement, and fractal patterns.
The inherent properties of Bezier curves[2] make them suitable for path prediction in the context of robot navigation. By utilizing a series of control points, Bezier curves can represent complex trajectories with smoothness and continuity. In the program presented, the observed data collected by the robot’s sensors is used to determine the control points for each segment of the Bezier curve.

   The Bezier curve formula is given by:


	 𝑃(𝑡)= ∑_(𝑖=0)^𝑛▒𝐵_𝑖^𝑛  (𝑡). 𝑃_𝑡                   …(i)

     〖      𝐵〗_𝑖^𝑛 (𝑡)=〖(■8(𝑛@𝑖)).𝑡〗^𝑖.〖(1−𝑡)〗^(𝑛−𝑖)            …(ii)

   	Equation (i) represents the Bezier curve formula, and Equation (ii) defines the binomial coefficient used in the     	formula.
![image](https://github.com/Prithwi007/Path_Prediction_of_a_Robot/assets/43519651/a27b2d1d-b3cc-4e83-95fb-fe6a90445f0c)



