import bpy

class BSP_PT_strip_infos(bpy.types.Panel):
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "strip"
    bl_label = ""

    @classmethod
    def poll(cls, context):
        strip = context.active_strip
        if not strip:
            return False
        if strip.type=="SCENE":
            return True
        elif strip.type=='IMAGE':
            return strip.bsp_properties.is_bsp

    def draw_header(self, context):
        layout = self.layout

        strip = context.active_strip
        if strip.type=="SCENE":
            layout.prop(strip.bsp_properties, "is_bsp", text="BSP")
        else:
            layout.label(text="BSP")

        op = layout.operator("BSP_OT_open_scene", icon="SCENE_DATA", text="")
        op.from_strip = True

    def draw(self, context):
        strip = context.active_strip
        props = strip.bsp_properties

        layout = self.layout
        layout.enabled = props.is_bsp

        layout.prop(props, "target_scene")
        layout.prop(props, "render_filepath")

### REGISTER ---
def register():
    bpy.utils.register_class(BSP_PT_strip_infos)

def unregister():
    bpy.utils.unregister_class(BSP_PT_strip_infos)
