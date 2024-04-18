#!/bin/bash
./run.sh $(./autotag llava) \
python3 -m nano_llm.agents.video_query --api=mlc \
--model Efficient-Large-Model/VILA-2.7b \
--max-context-len 768 \
--max-new-tokens 32 \
--video-input /dev/video0 \
--video-output webrtc://@:8554/output \
--nanodb /data/nanodb/coco/2017