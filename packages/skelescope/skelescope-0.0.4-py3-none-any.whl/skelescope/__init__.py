import importlib.metadata
import pathlib
import pandas as pd

import anywidget
import traitlets

try:
    __version__ = importlib.metadata.version("skelescope")   
except importlib.metadata.PackageNotFoundError:
    __version__ = "unknown"


def get_segments(swc_df, segments_meta):
    node_props = {}
    segments = {}

    for _, row in swc_df.iterrows():
        node_id = row.node_id
        node_props[node_id] = {
            "point": [row.x, row.y, row.z, row.radius],
            "parent": row.parent_id,
            "segments" : []
        }

    for segment_idx, segment in enumerate(segments_meta):
        assert len(segment) >= 2

        segments[segment_idx] = {
            "parent_segment" : -1,
            "children_segments" : [],
            "nodes": segment,
            "points" : []
        }
        for node in segment:
            node_props[node]["segments"].append(segment_idx)     

    for segment_idx, segment in segments.items():
        for node in segment["nodes"]:
            props = node_props[node]
            segment["points"].append(props["point"])

        segment_root_node = sorted(segment["nodes"])[0]
        parent_node_id = node_props[segment_root_node]["parent"]

        if(parent_node_id != -1):
            connected_segment_ids = set(node_props[parent_node_id]["segments"]) - set([segment_idx])
            if(len(connected_segment_ids)):
                parent_segment_id = connected_segment_ids.pop()
                segments[parent_segment_id]["children_segments"].append(segment_idx)
                segment["parent_segment"] = parent_segment_id 

    return segments
    


class Skelescope(anywidget.AnyWidget):
    _esm = pathlib.Path(__file__).parent / "static" / "widget.js"
    _css = pathlib.Path(__file__).parent / "static" / "widget.css"

    segments = traitlets.Dict({}).tag(sync=True)
    synapses = traitlets.List([]).tag(sync=True)
    
    selected_segments = traitlets.List([]).tag(sync=True)
    selected_synapses = traitlets.List([]).tag(sync=True)
    
    camera_target = traitlets.List([]).tag(sync=True)
    camera_position = traitlets.List([]).tag(sync=True)
    
    show_branches = traitlets.Bool(True).tag(sync=True)

    show_synapses = traitlets.Bool(True).tag(sync=True)
    synapse_radius = traitlets.Float(0.2).tag(sync=True)

    show_arrows = traitlets.Bool(False).tag(sync=True)
    arrow_length = traitlets.Float(3.0).tag(sync=True)
    arrow_shaft_radius = traitlets.Float(0.2).tag(sync=True)
    arrow_cone_radius = traitlets.Float(0.7).tag(sync=True)
    arrow_cone_position = traitlets.Float(0.6).tag(sync=True)
    arrow_offset_segment_ends = traitlets.Float(5.0).tag(sync=True)
    arrow_interval = traitlets.Float(7.0).tag(sync=True)

    def add_neuron(self, swc_df, synapse_df=None, segments_meta=None):
        if(segments_meta is None):
            raise NotImplementedError("segments_meta is required")
        
        self.segments = get_segments(swc_df, segments_meta)

        if synapse_df is not None:
            assert isinstance(synapse_df, pd.DataFrame)
            assert "x" in synapse_df.columns
            assert "y" in synapse_df.columns
            assert "z" in synapse_df.columns
            has_synapse_type = "type" in synapse_df.columns
            has_synapse_node_id = "node_id" in synapse_df.columns
            
            synapses_flat = []
            for _, row in synapse_df.iterrows():
                synapse = [row.x, row.y, row.z]

                if has_synapse_type:
                    synapse.append(row.type)
                else:
                    synapse.append("unknown") 
                
                if has_synapse_node_id:
                    synapse.append(row.node_id)
                else:
                    synapse.append(-1)

                synapses_flat.append(synapse)
            self.synapses = synapses_flat