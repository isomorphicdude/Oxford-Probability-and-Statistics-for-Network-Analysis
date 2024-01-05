import os
import glob
import argparse
import logging

parser = argparse.ArgumentParser(description='Remove aux files')
# if debug is true, then will not remove log files
parser.add_argument('--debug', 
                    action='store_true',
                    help='If true, will not remove log files')
# when flag added, will not remove pdf files
parser.add_argument('--not_remove_pdf',
                    action='store_true',
                    help='If true, will remove pdf files')

debug = parser.parse_args().debug
not_remove_pdf = parser.parse_args().not_remove_pdf

to_remove = ['aux', 'gz', 'fls', 'out', 
            'toc', 'blg', 'fdb_latexmk', 
        'bcf', 'xml', 'dvi', 'bbl']
    
if not debug:
    to_remove.append('log')

logging.basicConfig(
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

if __name__ == "__main__":
    if 'tex' in to_remove:
        raise Exception("\nDo not remove .tex\n")
    else:    
        for item in to_remove:            
            aux_list = glob.glob(f"**/*.{item}", recursive = True)
            for dir in aux_list:    
                try:
                    os.remove(dir)
                    logging.info(f"Removed: {dir}")
                except:
                    logging.warning(f"Failed to remove: {dir}")
                    
        # during editing, pdf is produced, which should be removed
        pdf_list = glob.glob(f"main/*.pdf", recursive = True)
        
        if not not_remove_pdf:
            for dir in pdf_list:    
                try:
                    os.remove(dir)
                    logging.info(f"Removed PDF file: {dir}")
                except:
                    logging.warning(f"Failed to remove {dir}")
                    
            # also remove the pdf in the root directory
            pdf_list = glob.glob(f"*.pdf", recursive=True)
            for dir in pdf_list:    
                try:
                    os.remove(dir)
                    logging.info(f"Removed PDF file: {dir}")
                except:
                    logging.warning(f"Failed to remove {dir}")
                
        logging.info("Done")