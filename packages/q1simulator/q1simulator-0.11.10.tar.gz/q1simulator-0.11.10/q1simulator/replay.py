import logging
import os

from qblox_instruments import Cluster
from .cluster import Cluster as SimCluster


logger = logging.getLogger(__name__)


_sim_counter = 0


# Q1Viewer
# Q1Plotter(cluster)
# .interval = (t_min, t_max)
# .channels = 
# .modules = 
# .reload()
# .plot()

def replay(cluster: Cluster,
           max_render_time=2e6,
           max_core_cycles=1e7,
           render_repetitions=False,
           skip_wait_sync=True,
           ):
    global _sim_counter
    _sim_counter += 1
    name = f'ClusterReplay_{_sim_counter}'

    modules = {}
    for slot, module in enumerate(cluster.modules, 1):
        if module.present():
            if module.is_qcm_type:
                sim_type = "QCM"
            elif module.is_qrm_type:
                sim_type = "QRM"
            else:
                logger.warning(f"unknown module type {module.module_type} in slot {slot}")
                continue
            if module.is_rf_type:
                sim_type += "_RF"
            modules[slot] = sim_type

    sim = SimCluster(name, modules)
    sim.config('max_render_time', max_render_time)
    sim.config('max_core_cycles', max_core_cycles)
    sim.config('render_repetitions', render_repetitions)
    sim.config('skip_wait_sync', skip_wait_sync)

    for slot, module in enumerate(sim.modules, 1):
        if module.present():
            cluster_mod = cluster.modules[slot-1]
            module.label = cluster_mod.label
            for iseq in range(6):
                cluster_seq = cluster_mod.sequencers[iseq]
                sim_seq = module.sequencers[iseq]
                enabled = _copy_settings(cluster_seq, sim_seq, module.is_qcm_type)
                if enabled:
                    print("arm", slot, iseq)
                    module.arm_sequencer(iseq)

    # TODO load raw / thresholded data from cluster
    # TODO add acquired values to plot.

    sim.start_sequencer()

    return sim


def _copy_settings(cluster_seq, sim_seq, is_qcm):
    sim_seq.sync_en(cluster_seq.sync_en.cache())
    if not sim_seq.sync_en():
        return False
    sequence = cluster_seq.sequence.cache()
    if not isinstance(sequence, dict):
        if not os.path.exists(sequence):
            raise Exception(f"Cannot load sequence {sequence}")
    sim_seq.sequence(sequence)
    sim_seq.label = cluster_seq.label

    param_names = [
            "mod_en_awg",
            "nco_freq",
            "connect_out0",
            "connect_out1",
            ]

    for i in range(1,16):
        param_names += [
            f'trigger{i}_count_threshold',
            f'trigger{i}_threshold_invert',
            ]

    if is_qcm:
        param_names += [
            "connect_out2",
            "connect_out3",
            ]
    else:
        param_names += [
            "demod_en_acq",
            "integration_length_acq",
            'thresholded_acq_rotation',
            'thresholded_acq_threshold',
            'thresholded_acq_trigger_en',
            'thresholded_acq_trigger_address',
            'thresholded_acq_trigger_invert',
            ]

    for param_name in param_names:
        value = getattr(cluster_seq, param_name).cache()
        if value is not None:
            sim_seq.set(param_name, value)

    return True

# %%

if False:
    from q1simulator.replay import replay
    sim = replay(context.station.Qblox)