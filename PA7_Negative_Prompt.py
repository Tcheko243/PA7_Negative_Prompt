class PA7_Negative_Prompt_Node():
    RETURN_TYPES = ("STRING",)
    FUNCTION = "get_negative_tags"
    CATEGORY = "Custom Nodes"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "option": (["UnRealistic", "AnimNegative"],)
            }
        }

    def get_negative_tags(self, option):
        tags = {
            "UnRealistic": "cgi, 3d, sketch, drawing, illustration, anime, digital art, painting, glitch, ugly, nude, nsfw, naked, bad hands, manga",
            "AnimNegative": "bad anatomy, blurry, bad proportions, cropped, disfigured, low quality, out of frame, watermark, jpeg artifacts"
        }
        return (tags.get(option, ""),)

NODE_CLASS_MAPPINGS = {
    "Photographer_Alpha7": PA7_Negative_Prompt_Node
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "Photographer_Alpha7": "PA7 Negative Prompts"
}
