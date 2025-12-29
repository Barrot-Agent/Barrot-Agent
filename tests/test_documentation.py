"""
Tests for documentation integrity
"""
import unittest
import os


class TestDocumentation(unittest.TestCase):
    """Test suite for documentation validation"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.repo_root = os.path.join(os.path.dirname(__file__), '..')
    
    def test_required_docs_exist(self):
        """Test that required documentation files exist"""
        required_docs = [
            'README.md',
            'DEPLOYMENT.md',
            'INGESTION_MANIFEST.md',
            'build_manifest.yaml'
        ]
        for doc in required_docs:
            doc_path = os.path.join(self.repo_root, doc)
            self.assertTrue(os.path.exists(doc_path), f"Missing required doc: {doc}")
    
    def test_readme_has_content(self):
        """Test that README has meaningful content"""
        readme_path = os.path.join(self.repo_root, 'README.md')
        with open(readme_path, 'r') as f:
            content = f.read()
            self.assertGreater(len(content), 100, "README is too short")
            self.assertIn('Barrot', content)
    
    def test_memory_bundles_directory(self):
        """Test that memory-bundles directory exists"""
        bundles_dir = os.path.join(self.repo_root, 'memory-bundles')
        self.assertTrue(os.path.isdir(bundles_dir))
    
    def test_site_directory_has_index(self):
        """Test that site directory has index.html"""
        site_dir = os.path.join(self.repo_root, 'site')
        index_path = os.path.join(site_dir, 'index.html')
        self.assertTrue(os.path.exists(index_path))


if __name__ == '__main__':
    unittest.main()
