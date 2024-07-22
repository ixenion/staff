// load and open 3dball scene from examples (https://github.com/Unity-Technologies/ml-agents)
// in cmd navigate to downloaded ml-agents and run:
// mlagents-learn config/ppo/3DBall.yaml --run-id=first3DBallRun (press enter twise)
// 3DBall.yaml is the default training configuration file provided by unity
// run-id is the unic name for this session
// then press play button in unity
// mean reward should increase
// to save model just again press play button

// to load copy first3DBallRun/3DBall.nn into unity TFModels folder
// and open 3DBall/agent inspector -> Behaviour Parameters -> Model -> 3DBall.nn

// to resume training:
// mlagents-learn config/ppo/3DBall.yaml --run-id=first3DBallRun --resume

// to observe training progress
// tensorboard --logdir results
// and navigate to localhost:6006

