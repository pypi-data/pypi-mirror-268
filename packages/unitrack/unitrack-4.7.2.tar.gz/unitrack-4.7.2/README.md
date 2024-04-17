# Unified Tracking in PyTorch

This package is a robust object tracking framework for PyTorch. It facilitates multi-stage and cascaded tracking algorithms under various modular configurations and assignment algorithms. This open-source implementation is designed to facilitate research in computer vision and machine learning. 

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Documentation](#documentation)
- [Contribution](#contribution)
- [Citation](#citation)
- [License](#license)
- [Recommendations](#recommendations)

## Installation

Ensure your environment meets the following requirements:

- `python >= 3.9`
- `torch >= 2.0`

Install via PyPI using the following command:

```bash
pip install unitrack
```

## Usage

The following example demonstrates object tracking across a sequence with detections that have `category` and `position` fields. This script tracks objects, updates internal state buffers for each frame, and prints the assigned IDs.

```python3
import unitrack

# Detections from 10 video frames having fields `category` and `position`.
frames = [
    {
        "category": torch.ones(1 + frame * 2, dtype=torch.long),
        "position": (torch.arange(1 + frame * 2, dtype=dtype)).unsqueeze(1),
    }
    for frame in range(0, 10)
]

# Multi-stage tracker with two value fields that map the detections' data
# to keys `pos_key` and `key_cat`, where the association stage calculates 
# the Euclidean distance of the positions between frames and subsequently 
# performs a Jonker-Volgenant assignment using the resulting cost matrix
tracker = unitrack.MultiStageTracker(
    fields={
        "key_pos": unitrack.fields.Value(key="category"),
        "key_cat": unitrack.fields.Value(key="position"),
    },
    stages=[unitrack.stages.Association(cost=costs.Distance("key_pos"), assignment=unitrack.assignment.Jonker(10))],
)

# Tracking memory that stores the relevant information to compute the
# cost matrix in the module buffers. States are observed at each frame,
# where in this case no state prediction is performed.
memory = unitrack.TrackletMemory(
    states={
        "key_pos": unitrack.states.Value(dtype),
        "key_cat": unitrack.states.Value(dtype=torch.long),
    }
)

# Iterate over frames, performing state observation, tracking and state
# propagation at every step.
for frame, detections in enumerate(frames):
    # Create a context object storing (meta)data about the current
    # frame, i.e. feature maps, instance detections and the frame number.
    ctx = unitrack.Context(None, detections, frame=frame)
    
    # Observe the states in memory. This can be extended to 
    # run a prediction step (e.g. Kalman filter) 
    obs = memory.observe()
    
    # Assign detections in the current frame to observations of
    # the state memory, giving an updated observations object
    # and the remaining unassigned new detections.
    obs, new = tracker(ctx, obs)
    
    # Update the tracking memory. Buffers are updated to match
    # the data in `obs`, and new IDs are generated for detection
    # data that could not be assigned in `new`. The returned tensor
    # contains ordered tracklet IDs for the detections assigned
    # to the frame context `ctx`.
    ids = tracks.update(ctx, obs, new)

    print(f"Assigned tracklet IDs {ids.tolist()} @ frame {frame}")
```

## Documentation

Technical documentation is provided inline with the source code.

## Contribution

Contributions that maintain backwards compatibility are welcome.

## Citation

If you utilize this package in your research, please cite the following paper:

```bib
@article{unifiedperception2023,
    title={Unified Perception: Efficient Depth-Aware Video Panoptic Segmentation with Minimal Annotation Costs},
    author={Kurt Stolle and Gijs Dubbelman},
    journal={arXiv preprint arXiv:2303.01991},
    year={2023}
}
```

Access the full paper [here](https://arxiv.org/abs/2303.01991).

## License

This project is licensed under [MIT License](LICENSE).

## Recommendations

The contents of this repository are designed for research purposes and is not recommended for use in production environments. It has not undergone testing for scalability or stability in a commercial context. Please use this tool within its intended scope.


