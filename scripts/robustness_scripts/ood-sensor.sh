source activate mllm-dev
categories=(
    "infrared"
    "lxray"
    "hxray"
    "mri"
    "ct"
    "remote"
    "driving"
)

for category in "${categories[@]}";
do
    CUDA_VISIBLE_DEVICES=0 python run_task.py --config mmte/configs/task/ood-sensor.yaml --cfg-options dataset_id="benchlmm-${category}" log_file="logs/robustness/ood-sensor-${category}.json"
done
