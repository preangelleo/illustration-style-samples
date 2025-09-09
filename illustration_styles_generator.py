#!/usr/bin/env python3
"""
Enhanced Cartoon Styles Test - Detailed Style Descriptions

Each cartoon style gets detailed, distinctive descriptions to ensure AI 
generates truly different visual styles.
"""

import asyncio
import os
import sys
import time
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Add project path to sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../vibe_coding/replicate_batch_process'))

from replicate_batch_process.intelligent_batch_processor import intelligent_batch_process

# Validate required environment variables
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")
if not REPLICATE_API_TOKEN:
    print("❌ Error: REPLICATE_API_TOKEN not found in environment variables")
    print("📝 Please create a .env file based on .env.example and add your Replicate API token")
    print("🔗 Get your token from: https://replicate.com/account/api-tokens")
    sys.exit(1)

# Set up environment variables
os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_TOKEN
os.environ["REPLICATE_GLOBAL_MAX_CONCURRENT"] = os.getenv("REPLICATE_GLOBAL_MAX_CONCURRENT", "300")

# Base character description - Adventure scene
BASE_CHARACTER = """An exciting cartoon adventure scene featuring a brave young explorer discovering a hidden treasure chest in an ancient mystical library. The scene shows floating magical books, glowing crystals, ornate golden treasures spilling from an old wooden chest, with mystical light beams streaming through tall arched windows. Ancient scrolls and mysterious artifacts are scattered around, creating an atmosphere of wonder and discovery."""

# Detailed style descriptions with specific visual characteristics
ENHANCED_CARTOON_STYLES = {
    "3D_Rendered_Cartoon_style": {
        "name": "3D Rendered Cartoon",
        "short_name": "3D_Rendered_Cartoon",  # Short name for file naming
        "description": f"""{BASE_CHARACTER}

STYLE: High-quality 3D rendered cartoon style similar to Pixar/DreamWorks animation. Volumetric lighting with realistic shadows and reflections. Smooth, polished surfaces with subtle subsurface scattering. Rich depth of field with cinematic camera angles. Clean, professional 3D modeling with soft ambient occlusion. Vibrant colors with realistic material properties - romantic couple with expressive faces and realistic textures, workshop tools should have realistic metallic and wood materials."""
    },
    
    "Anime_style": {
        "name": "Japanese Anime",
        "short_name": "Anime",
        "description": f"""{BASE_CHARACTER}

STYLE: Traditional Japanese anime/manga art style. Large expressive eyes with detailed highlights and reflections. Clean cel-shaded coloring with bold outlines. Dynamic romantic poses with exaggerated expressions. Vibrant, saturated colors typical of anime. Sharp, angular features with stylized proportions. Romantic couple in anime style with typical shoujo/romance manga aesthetic. Magical effects should have typical anime sparkle and energy patterns."""
    },
    
    "Chibi_style": {
        "name": "Chibi Cute",
        "short_name": "Chibi",
        "description": f"""{BASE_CHARACTER}

STYLE: Super deformed chibi style - extremely cute with oversized head (about 1/3 of total body height). Tiny body with stubby limbs. Enormous sparkling eyes taking up most of the face. Soft, round features with no sharp edges. Pastel color palette with soft, puffy textures. Everything should look adorable and kawaii. Simplified details but maximum cuteness factor."""
    },
    
    "Comic_Book_style": {
        "name": "American Comic Book",
        "short_name": "Comic_Book",
        "description": f"""{BASE_CHARACTER}

STYLE: Classic American comic book illustration style. Bold, thick black outlines around all objects. Ben-Day dot shading patterns and halftone effects. Dynamic action poses with motion lines. Vibrant primary colors (red, blue, yellow) with high contrast. Speech bubble aesthetic even without text. Strong shadows and highlights for dramatic effect. Vintage 1960s Marvel/DC comic book appearance."""
    },
    
    "Cyberpunk Cartoon style": {
        "name": "Cyberpunk Neon Cartoon",
        "short_name": "Cyberpunk",
        "description": f"""{BASE_CHARACTER}

STYLE: Dark cyberpunk aesthetic with neon cartoon elements. Glowing neon outlines in electric blue, hot pink, and acid green. Dark, moody background with holographic displays. Robot should have cybernetic enhancements and LED strips. Workshop filled with high-tech gadgets and floating holograms. Synthwave color palette with purple and teal tones. Futuristic graffiti-style details."""
    },
    
    "Fantasy Cartoon style": {
        "name": "Medieval Fantasy Cartoon",
        "short_name": "Fantasy",
        "description": f"""{BASE_CHARACTER}

STYLE: Medieval fantasy cartoon style with magical elements. Robot designed as a magical golem or enchanted automaton. Workshop as an alchemist's laboratory with crystal balls, spell books, and mystical ingredients. Warm, golden lighting from magical sources. Ornate decorative elements with Celtic or medieval patterns. Earth tones with magical purple and gold accents. Whimsical fairy-tale book illustration aesthetic."""
    },
    
    "Flat_Illustration_style": {
        "name": "Modern Flat Design",
        "short_name": "Flat_Illustration",
        "description": f"""{BASE_CHARACTER}

STYLE: Clean, minimal flat design illustration. No gradients, shadows, or 3D effects. Bold, solid colors with geometric shapes. Simplified forms with clean lines. Modern vector art aesthetic. Balanced composition with plenty of white space. Contemporary color scheme with muted, sophisticated tones. Everything should look like it belongs in a modern app or website design."""
    },
    
    "Minimalist Cartoon style": {
        "name": "Ultra Minimalist",
        "short_name": "Minimalist",
        "description": f"""{BASE_CHARACTER}

STYLE: Extremely simplified minimalist cartoon. Reduce all details to essential shapes only. Maximum 3-4 colors total. Clean geometric forms with minimal detail. Think simple emoji or pictogram style. Robot as basic circles and rectangles. Workshop elements as simple symbolic shapes. Lots of negative space. Ultra-clean, almost abstract representation."""
    },
    
    "Noir Cartoon style": {
        "name": "Film Noir Cartoon",
        "short_name": "Noir",
        "description": f"""{BASE_CHARACTER}

STYLE: Dark, moody film noir aesthetic in cartoon form. High contrast black and white with selective color accents. Dramatic shadows and venetian blind lighting effects. Detective story atmosphere. Robot as a 1940s-style detective character. Workshop as a dimly lit private investigator's office. Cigarette smoke effects (stylized). Classic noir cinematography angles."""
    },
    
    "Pastel Goth Style": {
        "name": "Pastel Goth Aesthetic",
        "short_name": "Pastel_Goth",
        "description": f"""{BASE_CHARACTER}

STYLE: Cute but dark pastel goth aesthetic. Soft pastel colors (lavender, mint green, baby pink) combined with gothic elements. Robot with adorable gothic accessories like tiny bat wings or skull decorations. Workshop with cute but spooky elements - friendly ghosts, kawaii skulls, pastel crystals. Soft, dreamy lighting with a slight dark romantic atmosphere."""
    },
    
    "Pixar_style": {
        "name": "Pixar Animation Studio",
        "short_name": "Pixar",
        "description": f"""{BASE_CHARACTER}

STYLE: Authentic Pixar Animation Studios style. Highly detailed 3D rendering with perfect subsurface scattering on organic materials. Warm, emotional character design with subtle facial expressions. Advanced lighting techniques with realistic caustics and global illumination. Rich textures and materials. Characters designed to convey personality through shape language. Professional theatrical animation quality."""
    },
    
    "Pop Art style": {
        "name": "Pop Art Movement",
        "short_name": "Pop_Art",
        "description": f"""{BASE_CHARACTER}

STYLE: 1960s Pop Art movement style like Andy Warhol or Roy Lichtenstein. Bold, vibrant colors with high contrast. Ben-day dots and halftone patterns. Multiple color variations like a Warhol print. Strong graphic design elements. Commercial art aesthetic. Flat, poster-like composition with bold typography feel even without text."""
    },
    
    "Rubber_Hose_style": {
        "name": "1930s Rubber Hose Animation",
        "short_name": "Rubber_Hose",
        "description": f"""{BASE_CHARACTER}

STYLE: Classic 1930s rubber hose animation style like early Mickey Mouse or Betty Boop. Characters with curved, flexible limbs that look like rubber hoses. Simple, rounded shapes with pie-cut eyes. Black and white with selective color. Bouncy, energetic poses. Hand-drawn animation aesthetic with slight imperfections. Vintage cartoon studio quality."""
    },
    
    "Sketch_Cartoon_style": {
        "name": "Hand-Drawn Sketch",
        "short_name": "Sketch",
        "description": f"""{BASE_CHARACTER}

STYLE: Rough hand-drawn sketch aesthetic. Visible pencil strokes and construction lines. Loose, gestural drawing style. Sketchy shading with cross-hatching. Slightly imperfect lines that show the artist's hand. Unfinished, work-in-progress appearance. Traditional animation cleanup style. Authentic hand-drawn character."""
    },
    
    "Steampunk Cartoon style": {
        "name": "Victorian Steampunk Cartoon",
        "short_name": "Steampunk",
        "description": f"""{BASE_CHARACTER}

STYLE: Victorian steampunk aesthetic with brass, copper, and bronze materials. Robot with visible gears, steam pipes, and clockwork mechanisms. Workshop filled with Victorian-era machinery and inventions. Warm sepia and brass color palette. Gothic Victorian architecture elements. Steam effects and mechanical details everywhere. Jules Verne adventure book illustration style."""
    },
    
    "Surreal Cartoon style": {
        "name": "Surrealist Art Movement",
        "short_name": "Surreal",
        "description": f"""{BASE_CHARACTER}

STYLE: Salvador Dalí-inspired surrealist cartoon. Melting, impossible geometry and dream-like elements. Robot with surreal modifications like melting parts or impossible mechanical configurations. Workshop defying physics with floating objects, warped perspective, and optical illusions. Vivid, otherworldly colors. Reality-bending visual elements."""
    },
    
    "Watercolor_Cartoon_style": {
        "name": "Traditional Watercolor Painting",
        "short_name": "Watercolor",
        "description": f"""{BASE_CHARACTER}

STYLE: Traditional watercolor painting technique. Soft, flowing colors that blend naturally. Visible paper texture and watercolor bleeding effects. Loose, organic brush strokes. Transparent layers with natural color mixing. Slight color bleeding outside lines. Hand-painted illustration book aesthetic. Soft, dreamy atmosphere with natural watercolor imperfections."""
    }
}

# Models to test (4 models final test - removed flux-kontext-max which requires input_image)
TEST_MODELS = [
    "black-forest-labs/flux-dev",           # Flux Dev - pure text-to-image, supports aspect_ratio
    "black-forest-labs/flux-1.1-pro-ultra", # Flux 1.1 Pro Ultra - supports aspect_ratio  
    "qwen/qwen-image",                      # supports aspect_ratio (16:9)
    "google/nano-banana"                    # only supports square 1024x1024
]

# Output directories configuration
DEFAULT_OUTPUT_DIR = "./output"
COMPATIBILITY_TEST_DIR = os.path.join(DEFAULT_OUTPUT_DIR, "compatibility_test")
PRESSURE_TEST_DIR = os.path.join(DEFAULT_OUTPUT_DIR, "pressure_test_300concurrent")

def ensure_output_directories():
    """Create all necessary output directories"""
    print("📁 Creating output directories...")
    
    # Create base directories
    os.makedirs(DEFAULT_OUTPUT_DIR, exist_ok=True)
    os.makedirs(COMPATIBILITY_TEST_DIR, exist_ok=True) 
    os.makedirs(PRESSURE_TEST_DIR, exist_ok=True)
    
    # Create model-specific subdirectories
    for model in TEST_MODELS:
        clean_name = get_clean_model_name(model)
        
        # Compatibility test directories
        compat_dir = os.path.join(COMPATIBILITY_TEST_DIR, clean_name)
        os.makedirs(compat_dir, exist_ok=True)
        
        # Pressure test directories  
        pressure_dir = os.path.join(PRESSURE_TEST_DIR, clean_name)
        os.makedirs(pressure_dir, exist_ok=True)
        
    print("✅ All output directories created successfully!")
    print(f"   📂 Compatibility tests: {COMPATIBILITY_TEST_DIR}")
    print(f"   📂 Pressure tests: {PRESSURE_TEST_DIR}")
    return COMPATIBILITY_TEST_DIR, PRESSURE_TEST_DIR

def create_enhanced_style_prompt(style_info):
    """Create enhanced prompt with detailed style description"""
    return style_info["description"]

def get_clean_model_name(model_name):
    """Extract clean model name for folder creation (remove company prefix)"""
    if "/" in model_name:
        return model_name.split("/")[-1]  # Get part after slash
    return model_name

async def test_single_model_single_style(model_name, style_key, base_output_dir):
    """Test single model with single style to verify functionality"""
    style_info = ENHANCED_CARTOON_STYLES[style_key]
    prompt = create_enhanced_style_prompt(style_info)
    
    # Create model-specific subfolder
    clean_model_name = get_clean_model_name(model_name)
    model_output_dir = os.path.join(base_output_dir, clean_model_name)
    
    print(f"🧪 Testing: {model_name} with {style_info['name']}")
    print(f"📁 Output folder: {model_output_dir}")
    
    try:
        # google/nano-banana only supports square format, qwen/qwen-image supports 16:9
        if model_name == "google/nano-banana":
            # nano-banana only supports square 1024x1024, no aspect_ratio parameter
            files = await intelligent_batch_process(
                prompts=[prompt],
                model_name=model_name,
                max_concurrent=1,
                output_dir=model_output_dir,
                num_outputs=1
            )
        elif model_name == "qwen/qwen-image":
            # qwen supports aspect_ratio parameter with 16:9 option
            files = await intelligent_batch_process(
                prompts=[prompt],
                model_name=model_name,
                max_concurrent=1,
                output_dir=model_output_dir,
                aspect_ratio="16:9",
                num_outputs=1,
                guidance=4,
                num_inference_steps=50
            )
        elif model_name == "black-forest-labs/flux-dev":
            # Flux Dev - Use exact same parameters as debug test
            files = await intelligent_batch_process(
                prompts=[prompt],
                model_name=model_name,
                max_concurrent=1,
                output_dir=model_output_dir,
                aspect_ratio="16:9",
                guidance=3.0,
                num_outputs=1,
                go_fast=True,
                output_format="jpg"
                # Removed megapixels="1" parameter to avoid conflict
            )
        elif model_name == "black-forest-labs/flux-1.1-pro-ultra":
            # Flux 1.1 Pro Ultra - Use exact same parameters as debug test
            files = await intelligent_batch_process(
                prompts=[prompt],
                model_name=model_name,
                max_concurrent=1,
                output_dir=model_output_dir,
                aspect_ratio="16:9",
                output_format="jpg",
                safety_tolerance=2,
                raw=False
            )
        else:
            # Default fallback
            files = await intelligent_batch_process(
                prompts=[prompt],
                model_name=model_name,
                max_concurrent=1,
                output_dir=model_output_dir,
                num_outputs=1
            )
        
        if files and files[0]:
            # Rename files using cartoon style names
            original_file = files[0]
            if os.path.exists(original_file):
                file_ext = os.path.splitext(original_file)[1]
                new_filename = f"{style_info['short_name']}_compatibility_{clean_model_name}{file_ext}"
                new_file_path = os.path.join(model_output_dir, new_filename)
                
                # Rename file
                os.rename(original_file, new_file_path)
                print(f"✅ {model_name} - {style_info['name']}: SUCCESS → {new_filename}")
                return True, new_file_path
            else:
                print(f"✅ {model_name} - {style_info['name']}: SUCCESS")
                return True, files[0]
        else:
            print(f"❌ {model_name} - {style_info['name']}: NO FILE GENERATED")
            return False, None
            
    except Exception as e:
        print(f"❌ {model_name} - {style_info['name']}: ERROR - {str(e)}")
        return False, None

async def run_model_compatibility_test():
    """Test each model with first style to ensure compatibility"""
    print("🔧 PHASE 1: Model Compatibility Test")
    print("="*60)
    
    output_dir = "/Users/lgg/coding/vibe_coding/replicate_batch_process/output/compatibility_test"
    first_style = "3D_Rendered_Cartoon_style"  # Test with first style
    
    successful_models = []
    
    for model in TEST_MODELS:
        success, file_path = await test_single_model_single_style(model, first_style, output_dir)
        if success:
            successful_models.append(model)
        
        # Small delay between tests
        await asyncio.sleep(2)
    
    print(f"\n📊 Compatibility Test Results:")
    print(f"✅ Successful models: {len(successful_models)}/{len(TEST_MODELS)}")
    for model in successful_models:
        print(f"   ✅ {model}")
    
    failed_models = [m for m in TEST_MODELS if m not in successful_models]
    if failed_models:
        print(f"❌ Failed models:")
        for model in failed_models:
            print(f"   ❌ {model}")
    
    return successful_models

async def run_large_scale_pressure_test(successful_models):
    """Run large scale pressure test with all models and all 17 styles - 300 concurrent!"""
    print(f"\n🚀 PHASE 2: Final Test - {len(successful_models)} Models × 17 Styles = {len(successful_models) * len(ENHANCED_CARTOON_STYLES)} Images")
    print("="*60)
    
    # Print overall start time
    overall_start_time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"📅 [Overall test start time] {overall_start_time_str}")
    
    start_time = time.time()
    
    total_images = len(successful_models) * len(ENHANCED_CARTOON_STYLES)
    print(f"📊 Final Test Scale: {len(successful_models)} models × {len(ENHANCED_CARTOON_STYLES)} styles = {total_images} images")
    print(f"🔄 Models: {', '.join([get_clean_model_name(m) for m in successful_models])}")
    print(f"🌐 Global concurrency limit: 300 - MAXIMUM EFFICIENCY!")
    print(f"🚀 Using 300 concurrent requests for maximum speed!")
    
    output_dir = "/Users/lgg/coding/vibe_coding/replicate_batch_process/output/pressure_test_300concurrent"
    
    # Process each model separately with MAXIMUM 300 concurrent processing
    results = []
    
    for model_idx, model in enumerate(successful_models):
        print(f"\n🤖 [{model_idx+1}/{len(successful_models)}] Processing model: {model}")
        clean_model_name = get_clean_model_name(model)
        model_output_dir = os.path.join(output_dir, clean_model_name)
        
        # Create all prompts for this model with predefined output filenames
        prompt_requests = []
        output_filepaths = []
        style_mappings = []  # Keep as list since we can now rely on filename order
        
        for style_idx, (style_key, style_info) in enumerate(ENHANCED_CARTOON_STYLES.items()):
            prompt = create_enhanced_style_prompt(style_info)
            prompt_requests.append(prompt)
            
            # Predefine output filenames for precise matching
            output_filename = f"{style_info['short_name']}_{clean_model_name}.jpg"
            output_filepath = os.path.join(model_output_dir, output_filename)
            output_filepaths.append(output_filepath)
            
            # Store style info in corresponding order
            style_mappings.append({
                'style_idx': style_idx,
                'style_key': style_key,
                'style_name': style_info['name'],
                'short_name': style_info['short_name'],
                'expected_file': output_filepath
            })
        
        print(f"📝 Generated {len(prompt_requests)} prompts for {model}")
        print(f"📁 Saving to: {model_output_dir}")
        print(f"⚡ Using 300 CONCURRENT requests for maximum speed!")
        
        start_model_time = time.time()
        
        try:
            # Use 300 concurrent requests to process all 17 styles - Use predefined filenames for precise matching!
            # Print model start time
            model_start_time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"🚀 [{model_start_time_str}] Starting {model} - Processing {len(prompt_requests)} images...")
            
            if model == "google/nano-banana":
                # nano-banana only supports square format, no aspect_ratio parameter needed
                files = await intelligent_batch_process(
                    prompts=prompt_requests,
                    model_name=model,
                    max_concurrent=300,
                    output_dir=model_output_dir,
                    output_filepath=output_filepaths,  # Use predefined filenames
                    num_outputs=1
                )
            elif model == "qwen/qwen-image":
                # Qwen - Precise parameter settings to ensure 16:9 output
                files = await intelligent_batch_process(
                    prompts=prompt_requests,
                    model_name=model,
                    max_concurrent=300,
                    output_dir=model_output_dir,
                    output_filepath=output_filepaths,  # Use predefined filenames
                    aspect_ratio="16:9",  # Explicitly specify 16:9
                    guidance=4.0,
                    num_inference_steps=50,
                    output_format="jpg",
                    output_quality=90,
                    image_size="optimize_for_quality",
                    enhance_prompt=False,
                    go_fast=True
                )
            elif model == "black-forest-labs/flux-dev":
                # Flux Dev - Use exact same parameters as debug test
                files = await intelligent_batch_process(
                    prompts=prompt_requests,
                    model_name=model,
                    max_concurrent=300,
                    output_dir=model_output_dir,
                    output_filepath=output_filepaths,  # Use predefined filenames
                    aspect_ratio="16:9",
                    guidance=3.0,
                    num_outputs=1,
                    go_fast=True,
                    output_format="jpg"
                    # Removed megapixels="1" parameter
                )
            elif model == "black-forest-labs/flux-1.1-pro-ultra":
                # Flux 1.1 Pro Ultra - Precise parameter settings to ensure 16:9 output
                files = await intelligent_batch_process(
                    prompts=prompt_requests,
                    model_name=model,
                    max_concurrent=300,
                    output_dir=model_output_dir,
                    output_filepath=output_filepaths,  # Use predefined filenames
                    aspect_ratio="16:9",  # Explicitly specify 16:9
                    output_format="jpg",
                    safety_tolerance=2,
                    raw=False
                )
            else:
                # Default fallback
                files = await intelligent_batch_process(
                    prompts=prompt_requests,
                    model_name=model,
                    max_concurrent=300,
                    output_dir=model_output_dir,
                    output_filepath=output_filepaths,  # Use predefined filenames
                    num_outputs=1
                )
            
            model_duration = time.time() - start_model_time
            successful_files = [f for f in files if f]
            
            # Print model end time
            model_end_time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"✅ [{model_end_time_str}] {model} completed: {len(successful_files)}/{len(prompt_requests)} images in {model_duration:.1f}s")
            print(f"⚡ Speed: {len(successful_files)/model_duration:.2f} images/second!")
            
            # Verify file generation results - Files already have correct names!
            print(f"🔧 Verifying generated files...")
            print(f"📊 Files returned: {len(files)}, Expected: {len(style_mappings)}")
            
            # Check if each expected file was generated successfully
            for i, style_mapping in enumerate(style_mappings):
                expected_file = style_mapping['expected_file']
                
                if expected_file in files and os.path.exists(expected_file):
                    # File generated successfully, no renaming needed!
                    results.append({
                        'success': True,
                        'model': model,
                        'style': style_mapping['style_name'],
                        'short_name': style_mapping['short_name'],
                        'original_file': expected_file,
                        'renamed_file': expected_file  # File already has correct name
                    })
                    print(f"   ✅ [{i:2d}] {style_mapping['short_name']} → {os.path.basename(expected_file)}")
                    
                else:
                    # File generation failed
                    results.append({
                        'success': False,
                        'model': model,
                        'style': style_mapping['style_name'],
                        'short_name': style_mapping['short_name'],
                        'error': 'File not generated'
                    })
                    print(f"   ❌ [{i:2d}] {style_mapping['short_name']} → File not generated")
            
            # Check for unexpected additional files
            expected_files = set(mapping['expected_file'] for mapping in style_mappings)
            actual_files = set(files)
            unexpected_files = actual_files - expected_files
            
            if unexpected_files:
                print(f"   ⚠️ Unexpected files generated: {len(unexpected_files)}")
                for unexpected_file in unexpected_files:
                    print(f"      - {os.path.basename(unexpected_file)}")
        
        except Exception as e:
            print(f"❌ {model} failed: {str(e)}")
            for style_mapping in style_mappings.values():
                results.append({
                    'success': False,
                    'model': model,
                    'style': style_mapping['style_name'],
                    'short_name': style_mapping['short_name'],
                    'error': str(e)
                })
        
        print(f"⏱️  Model {model} processing time: {time.time() - start_model_time:.1f}s")
    
    # Calculate final results
    total_duration = time.time() - start_time
    successful_results = [r for r in results if r['success']]
    
    # Print overall end time
    overall_end_time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n🎉 Large scale 300 concurrent pressure test completed!")
    print(f"📅 [Overall test end time] {overall_end_time_str}")
    print(f"⏱️  Total time: {total_duration:.2f} seconds")
    print(f"📄 Successfully generated: {len(successful_results)} / {len(results)} images")
    print(f"📈 Success rate: {len(successful_results)/len(results)*100:.1f}%")
    print(f"⚡ 平均每张图片用时: {total_duration/len(results):.2f} 秒")
    print(f"🚀 图片生成速率: {len(results)/total_duration:.2f} 张/秒")
    
    # Generate summary by model
    print(f"\n📊 分模型结果统计:")
    for model in successful_models:
        model_results = [r for r in results if r['model'] == model]
        model_successes = [r for r in model_results if r['success']]
        clean_name = get_clean_model_name(model)
        print(f"   🤖 {clean_name}: {len(model_successes)}/{len(model_results)} ({len(model_successes)/len(model_results)*100:.1f}%)")
    
    # Create detailed summary report
    summary_file = os.path.join(output_dir, "300concurrent_pressure_test_summary.txt")
    os.makedirs(output_dir, exist_ok=True)
    
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write("300 Concurrent Large Scale Pressure Test Report\n")
        f.write("=" * 50 + "\n")
        f.write(f"Test time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Concurrency setting: 300 (maximum concurrent)\n")
        f.write(f"Total images: {len(results)}\n")
        f.write(f"Successfully generated: {len(successful_results)}\n")
        f.write(f"Failed count: {len(results) - len(successful_results)}\n")
        f.write(f"Success rate: {len(successful_results)/len(results)*100:.1f}%\n")
        f.write(f"Total time: {total_duration:.2f} seconds\n")
        f.write(f"Generation rate: {len(results)/total_duration:.2f} images/sec\n\n")
        
        f.write("Detailed results:\n")
        f.write("-" * 30 + "\n")
        for result in results:
            status = "✅ Success" if result['success'] else "❌ Failed"
            f.write(f"{result['short_name']} ({get_clean_model_name(result['model'])}): {status}\n")
            if result['success'] and 'renamed_file' in result:
                f.write(f"  File: {os.path.basename(result['renamed_file'])}\n")
            elif not result['success'] and 'error' in result:
                f.write(f"  Error: {result['error']}\n")
            f.write("\n")
    
    print(f"\n📝 Detailed report saved to: {summary_file}")
    
    return results

async def main():
    """Main test function"""
    import sys
    
    # Create output directories first
    ensure_output_directories()
    
    # Command line argument processing
    compatibility_only = "--compatibility-only" in sys.argv
    skip_compatibility = "--skip-compatibility" in sys.argv
    
    print("🎨 Enhanced Cartoon Styles Final Test")
    
    if compatibility_only:
        print("🧪 COMPATIBILITY TEST ONLY MODE")
        print("="*60)
        
        # Run compatibility test only
        successful_models = await run_model_compatibility_test()
        
        if successful_models:
            print(f"\n✅ Compatibility test completed! {len(successful_models)}/{len(TEST_MODELS)} models passed test")
        else:
            print(f"\n❌ Compatibility test failed! No models passed test")
        return
        
    elif skip_compatibility:
        print("🚀 SKIP COMPATIBILITY - DIRECT PRESSURE TEST")
        print("🧪 4 Models × 17 Styles = 68 Images Total")  
        print("="*60)
        
        # Skip compatibility test, use all models directly
        successful_models = TEST_MODELS
        print(f"🤖 Using all {len(successful_models)} models: {[get_clean_model_name(m) for m in successful_models]}")
        
    else:
        # Default: compatibility test first, then user confirmation
        print("🧪 4 Models × 17 Styles = 68 Images Total")
        print("="*60)
        
        # Phase 1: Model compatibility test
        successful_models = await run_model_compatibility_test()
        
        if not successful_models:
            print("❌ No models passed compatibility test! Cannot proceed.")
            return
        
        # Ask user whether to continue with pressure test
        print(f"\n🤔 {len(successful_models)} models passed compatibility test.")
        print("📝 Continue with pressure test? (y/N): ", end="", flush=True)
        response = input().strip().lower()
        
        if response not in ['y', 'yes']:
            print("🛑 Pressure test cancelled by user.")
            return
            
        print(f"✅ Starting pressure test: {len(successful_models)} models × 17 styles = {len(successful_models) * 17} images...")
    
    # Phase 2: Final pressure test
    results = await run_large_scale_pressure_test(successful_models)
    
    if results:
        print(f"\n✨ All testing completed! Check output folders for results.")
    else:
        print(f"\n😞 Pressure test encountered issues")

if __name__ == "__main__":
    asyncio.run(main())