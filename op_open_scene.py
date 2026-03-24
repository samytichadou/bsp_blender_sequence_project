import bpy

class BSP_OT_open_scene(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "bsp.open_scene"
    bl_label = "Open Scene"
    bl_options = {'INTERNAL'}

    from_strip: bpy.props.BoolProperty()

    @classmethod
    def poll(cls, context):
        if context.active_strip is not None:
            return context.active_strip.bsp_properties.target_scene

    def execute(self, context):
        origin_props = context.window_manager.bsp_origin_scene

        target_scene = context.active_strip.bsp_properties.target_scene


        # Check if target scene exists

        # Store origin scene
        origin_scene = context.sequencer_scene
        origin_props.scene_name = origin_scene.name
        origin_props.workspace_name = context.window.workspace.name
        # context.window_manager.bsp_origin_scene.scene_name =

        # Change layout
        context.window.workspace = bpy.data.workspaces['Layout']

        # Open scene
        bpy.context.window.scene = target_scene

        self.report({'INFO'}, "Scene opened")

        return {'FINISHED'}


### REGISTER ---
def register():
    bpy.utils.register_class(BSP_OT_open_scene)

def unregister():
    bpy.utils.unregister_class(BSP_OT_open_scene)
