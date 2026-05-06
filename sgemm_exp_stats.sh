python3.11 trace_extraction.py ../sgemm_lrr/sgemm_5l ./sgemm_traces_lrr/sgemm_5l
python3.11 trace_extraction.py ../sgemm_lrr/sgemm_10l ./sgemm_traces_lrr/sgemm_10l
python3.11 trace_extraction.py ../sgemm_lrr/sgemm_25l ./sgemm_traces_lrr/sgemm_25l
python3.11 trace_extraction.py ../sgemm_lrr/sgemm_50l ./sgemm_traces_lrr/sgemm_50l
python3.11 trace_extraction.py ../sgemm_lrr/sgemm_100l ./sgemm_traces_lrr/sgemm_100l
python3.11 trace_extraction.py ../sgemm_lrr/sgemm_200l ./sgemm_traces_lrr/sgemm_200l
python3.11 trace_extraction.py ../sgemm_lrr/sgemm_400l ./sgemm_traces_lrr/sgemm_400l

python3.11 trace_extraction.py ../sgemm_gto/sgemm_5l ./sgemm_traces_gto/sgemm_5l
python3.11 trace_extraction.py ../sgemm_gto/sgemm_10l ./sgemm_traces_gto/sgemm_10l
python3.11 trace_extraction.py ../sgemm_gto/sgemm_25l ./sgemm_traces_gto/sgemm_25l
python3.11 trace_extraction.py ../sgemm_gto/sgemm_50l ./sgemm_traces_gto/sgemm_50l
python3.11 trace_extraction.py ../sgemm_gto/sgemm_100l ./sgemm_traces_gto/sgemm_100l
python3.11 trace_extraction.py ../sgemm_gto/sgemm_200l ./sgemm_traces_gto/sgemm_200l
python3.11 trace_extraction.py ../sgemm_gto/sgemm_400l ./sgemm_traces_gto/sgemm_400l


python3.11 worst_traces_extraction.py ./sgemm_traces_lrr/sgemm_5l ./ptx_files ./sgemm_bounds ./exp_sgemm_lrr
python3.11 worst_traces_extraction.py ./sgemm_traces_lrr/sgemm_10l ./ptx_files ./sgemm_bounds ./exp_sgemm_lrr
python3.11 worst_traces_extraction.py ./sgemm_traces_lrr/sgemm_25l ./ptx_files ./sgemm_bounds ./exp_sgemm_lrr
python3.11 worst_traces_extraction.py ./sgemm_traces_lrr/sgemm_50l ./ptx_files ./sgemm_bounds ./exp_sgemm_lrr
python3.11 worst_traces_extraction.py ./sgemm_traces_lrr/sgemm_100l ./ptx_files ./sgemm_bounds ./exp_sgemm_lrr
python3.11 worst_traces_extraction.py ./sgemm_traces_lrr/sgemm_200l ./ptx_files ./sgemm_bounds ./exp_sgemm_lrr
python3.11 worst_traces_extraction.py ./sgemm_traces_lrr/sgemm_400l ./ptx_files ./sgemm_bounds ./exp_sgemm_lrr

python3.11 worst_traces_extraction.py ./sgemm_traces_gto/sgemm_5l ./ptx_files ./sgemm_bounds ./exp_sgemm_gto
python3.11 worst_traces_extraction.py ./sgemm_traces_gto/sgemm_10l ./ptx_files ./sgemm_bounds ./exp_sgemm_gto
python3.11 worst_traces_extraction.py ./sgemm_traces_gto/sgemm_25l ./ptx_files ./sgemm_bounds ./exp_sgemm_gto
python3.11 worst_traces_extraction.py ./sgemm_traces_gto/sgemm_50l ./ptx_files ./sgemm_bounds ./exp_sgemm_gto
python3.11 worst_traces_extraction.py ./sgemm_traces_gto/sgemm_100l ./ptx_files ./sgemm_bounds ./exp_sgemm_gto
python3.11 worst_traces_extraction.py ./sgemm_traces_gto/sgemm_200l ./ptx_files ./sgemm_bounds ./exp_sgemm_gto
python3.11 worst_traces_extraction.py ./sgemm_traces_gto/sgemm_400l ./ptx_files ./sgemm_bounds ./exp_sgemm_gto


python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_5l_lrr/gpgpusim.config ./exp_sgemm_lrr/sgemm_5l/ 2 ./sgemm_res.csv
python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_5l_gto/gpgpusim.config ./exp_sgemm_gto/sgemm_5l/ 2 ./sgemm_res.csv

python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_10l_lrr/gpgpusim.config ./exp_sgemm_lrr/sgemm_10l/ 2 ./sgemm_res.csv
python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_10l_gto/gpgpusim.config ./exp_sgemm_gto/sgemm_10l/ 2 ./sgemm_res.csv

python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_25l_lrr/gpgpusim.config ./exp_sgemm_lrr/sgemm_25l/ 2 ./sgemm_res.csv
python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_25l_gto/gpgpusim.config ./exp_sgemm_gto/sgemm_25l/ 2 ./sgemm_res.csv

python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_50l_lrr/gpgpusim.config ./exp_sgemm_lrr/sgemm_50l/ 2 ./sgemm_res.csv
python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_50l_gto/gpgpusim.config ./exp_sgemm_gto/sgemm_50l/ 2 ./sgemm_res.csv

python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_100l_lrr/gpgpusim.config ./exp_sgemm_lrr/sgemm_100l/ 2 ./sgemm_res.csv
python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_100l_gto/gpgpusim.config ./exp_sgemm_gto/sgemm_100l/ 2 ./sgemm_res.csv

python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_200l_lrr/gpgpusim.config ./exp_sgemm_lrr/sgemm_200l/ 2 ./sgemm_res.csv
python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_200l_gto/gpgpusim.config ./exp_sgemm_gto/sgemm_200l/ 2 ./sgemm_res.csv

python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_400l_lrr/gpgpusim.config ./exp_sgemm_lrr/sgemm_400l/ 2 ./sgemm_res.csv
python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_400l_gto/gpgpusim.config ./exp_sgemm_gto/sgemm_400l/ 2 ./sgemm_res.csv