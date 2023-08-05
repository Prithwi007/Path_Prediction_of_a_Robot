# Path_Prediction_of_a_Robot
The objective of this research is to predict the path of robot using a proposed algorithm. The environment consists of multiple observers placed at different locations, which can detect the position of the robots. However, the observers have limited range of vision, and they can only detect robots when they come within their predefined range.

The range of vision for each observer is circular, and the robots are detected when they enter this range. As a result, only a small portion of the robot's path can be observed using collision detection techniques. This path is generated periodically based on parameters such as depth, displacement, and fractal patterns.

![Figure_1](https://github.com/Prithwi007/Path_Prediction_of_a_Robot/assets/43519651/5ce8fbce-1a04-42cc-a112-318f9817fb6c)


# Bezier Curves for Path Prediction in Robot Navigation

The inherent properties of Bezier curves make them suitable for path prediction in the context of robot navigation. This README provides an overview of how Bezier curves can be utilized to represent complex trajectories with smoothness and continuity.

## Bezier Curve Formula

The Bezier curve formula is given by:

$P(t) = \sum_{i=0}^{n} B_i^n(t) \cdot P_t$    ...(i)

Where:
- \( P(t) \) represents the Bezier curve at parameter \( t \).
- \( B_i^n(t) \) is the binomial coefficient defined as \( \binom{n}{i} \cdot t^i \cdot (1-t)^{(n-i)} \).
- \( P_t \) are the control points used in the Bezier curve.
  
![bezier](https://github.com/Prithwi007/Path_Prediction_of_a_Robot/assets/43519651/aa5141cd-eabe-4e65-8774-1a744151868c)


## LSTM Model for Path Prediction
LSTM networks are a type of recurrent neural network (RNN) known for their ability to capture temporal dependencies in sequential data. In our robot navigation system, we employ LSTM networks to predict the robot's path by training the model on historical input-output sequences. The LSTM model learns sequential patterns in the data, enabling it to make predictions based on the context of previous data points.
The equation used in the given code for the LSTM model can be represented as:

\[ h_{t} = LSTM(x_{t}, h_{t-1}, c_{t-1}) \]
\[ y_{t} = Dense(h_{t}) \]

Where:
- \( x_{t} \) is the input sequence at time step \( t \).
- \( h_{t} \) is the hidden state of the LSTM layer at time step \( t \).
- \( c_{t} \) is the cell state of the LSTM layer at time step \( t \).
- \( y_{t} \) is the predicted output (x, y coordinates) at time step \( t \).

![lstm](https://github.com/Prithwi007/Path_Prediction_of_a_Robot/assets/43519651/da6fe9f6-4236-4328-9c33-e6d08a85f01b)


