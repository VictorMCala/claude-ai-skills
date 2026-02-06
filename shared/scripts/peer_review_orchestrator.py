#!/usr/bin/env python3
"""
Peer Review Orchestrator - Multi-Model Code Review

Gets code reviews from multiple AI models (Claude + GPT-4o) and synthesizes
their feedback into a comprehensive peer review report.

Usage:
    python peer_review_orchestrator.py <file_path> [--diff]
    python peer_review_orchestrator.py --help
"""

import os
import sys
import argparse
import json
from pathlib import Path
from typing import List, Dict, Any
from dotenv import load_dotenv

try:
    from litellm import completion
except ImportError:
    print("Error: litellm not installed. Run: pip install litellm")
    sys.exit(1)


# Load environment variables
script_dir = Path(__file__).parent
config_dir = script_dir.parent / "config"
env_file = config_dir / ".env"

if env_file.exists():
    load_dotenv(env_file)
else:
    print(f"Warning: .env file not found at {env_file}")


class PeerReviewOrchestrator:
    """Orchestrates multi-model peer review"""

    def __init__(self):
        self.models = self._get_available_models()

    def _get_available_models(self) -> List[str]:
        """Get list of available models based on configured API keys"""
        models = []

        # Claude Sonnet (assumed available via Claude Code)
        models.append("claude-sonnet-4-5-20250929")

        # Azure GPT-4o
        if os.getenv("AZURE_OPENAI_API_KEY"):
            models.append("azure/gpt-4o")

        if len(models) < 2:
            print("Warning: Less than 2 models available. Need at least 2 for peer review.")

        return models

    def read_code(self, file_path: str, is_diff: bool = False) -> str:
        """Read code from file or get git diff"""
        if is_diff:
            import subprocess
            result = subprocess.run(
                ["git", "diff", file_path],
                capture_output=True,
                text=True
            )
            if result.returncode != 0:
                raise Exception(f"Git diff failed: {result.stderr}")
            return result.stdout
        else:
            with open(file_path, 'r') as f:
                return f.read()

    def get_review(self, model: str, code: str, context: str = "") -> Dict[str, Any]:
        """Get code review from a specific model"""
        prompt = f"""You are performing a code review. Analyze the following code and provide:

1. **Bugs and Issues**: Any correctness problems, logic errors, or bugs
2. **Security Concerns**: Security vulnerabilities or risks
3. **Performance Issues**: Performance problems or inefficiencies
4. **Best Practices**: Code quality and best practice violations
5. **Positive Findings**: What's done well

{f"Context: {context}" if context else ""}

Code to review:
```
{code}
```

Provide your review in a structured format with specific line numbers where applicable.
Be constructive and specific."""

        try:
            response = completion(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3
            )
            return {
                "model": model,
                "review": response.choices[0].message.content,
                "success": True
            }
        except Exception as e:
            return {
                "model": model,
                "error": str(e),
                "success": False
            }

    def synthesize_reviews(self, reviews: List[Dict[str, Any]]) -> str:
        """Synthesize multiple reviews into one comprehensive report"""
        successful_reviews = [r for r in reviews if r.get("success")]

        if not successful_reviews:
            return "❌ All model reviews failed."

        # Build synthesis prompt
        reviews_text = "\n\n---\n\n".join([
            f"**Review from {r['model']}:**\n{r['review']}"
            for r in successful_reviews
        ])

        synthesis_prompt = f"""You have received code reviews from multiple AI models. Synthesize these into one comprehensive peer review report.

# Reviews from Peer Models:

{reviews_text}

---

# Your Task:

Create a unified peer review report that:
1. **Consolidates** common findings across models
2. **Highlights** unique insights from each model
3. **Prioritizes** issues by severity (Critical/Important/Nice-to-have)
4. **Resolves** any contradictions between reviews
5. **Provides** actionable recommendations

Format as:
```markdown
# Peer Review Report (Multi-Model)

## 🤝 Consensus Findings
[Issues all models agreed on]

## 🔴 Critical Issues
[Must fix - identified by any model]

## 🟡 Important Suggestions
[Should fix - identified by any model]

## 💡 Unique Insights
**From {model}:**
[Unique findings]

## ✅ Strengths Identified
[What multiple models praised]

## 📊 Model Agreement Analysis
[Where models agreed/disagreed]

## 🎯 Prioritized Actions
[Top recommendations]
```
"""

        try:
            # Use Claude for synthesis (most capable)
            synthesis = completion(
                model="claude-sonnet-4-5-20250929",
                messages=[{"role": "user", "content": synthesis_prompt}],
                temperature=0.3
            )
            return synthesis.choices[0].message.content
        except Exception as e:
            # Fallback: just concatenate reviews
            return f"""# Peer Review Report (Multi-Model)

{reviews_text}

---

*Note: Automatic synthesis failed, showing raw reviews. Error: {str(e)}*
"""

    def run_peer_review(self, file_path: str, is_diff: bool = False, context: str = "") -> str:
        """Run complete peer review process"""
        print(f"🔍 Reading code from: {file_path}")
        code = self.read_code(file_path, is_diff)

        if not code.strip():
            return "❌ No code to review (file empty or no diff)"

        print(f"👥 Running peer review with {len(self.models)} models...")

        reviews = []
        for model in self.models:
            print(f"  📝 Getting review from {model}...")
            review = self.get_review(model, code, context)
            reviews.append(review)

            if not review.get("success"):
                print(f"  ⚠️  {model} failed: {review.get('error')}")

        print("🔄 Synthesizing reviews...")
        final_report = self.synthesize_reviews(reviews)

        return final_report


def main():
    parser = argparse.ArgumentParser(
        description="Multi-model peer code review orchestrator"
    )
    parser.add_argument(
        "file_path",
        help="Path to file to review (or 'HEAD' for git diff)"
    )
    parser.add_argument(
        "--diff",
        action="store_true",
        help="Review git diff instead of full file"
    )
    parser.add_argument(
        "--context",
        default="",
        help="Additional context for reviewers"
    )
    parser.add_argument(
        "--output",
        help="Output file (default: stdout)"
    )

    args = parser.parse_args()

    orchestrator = PeerReviewOrchestrator()

    try:
        report = orchestrator.run_peer_review(
            args.file_path,
            is_diff=args.diff,
            context=args.context
        )

        if args.output:
            with open(args.output, 'w') as f:
                f.write(report)
            print(f"\n✅ Review saved to: {args.output}")
        else:
            print("\n" + "="*80)
            print(report)
            print("="*80)

    except Exception as e:
        print(f"❌ Error: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
